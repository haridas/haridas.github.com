Title: Pytorch model Inference pipeline using C++
Date: 2021-01-22  00:00
Category: data-science
Tags: pytroch,cpp
Authors: Haridas N

After seeing the option that we can easily export the PyTorch model and load it in
non-python environments like  C++ programs for better inference performance, I couldn't
wait to try this out. So here I’m explaining our recent experience with one of the
Pytorch models used with the [Pic2Card](https://www.prnewswire.com/news-releases/imaginea-launches-pic2card-automatic-images-to-card-converter-a-new-feature-in-microsoft-adaptive-cards-301089878.html) Project.

Pic2Card is our open source contribution to the [AdaptiveCards](https://adaptivecards.io/) community, where we are
employing multiple object detection models. One PyTorch model that we have played with is
[DETR](https://arxiv.org/abs/2005.12872) end-to-end transformer based object detection pipeline.
Here I will show how we can export the trained DETR model into a C++ pipeline for inference.

One thing to note here is that the c++ inference pipeline is possible because that PyTorch
has the C++ frontend to their Tensor library named it as [libtorch](https://pytorch.org/cppdocs/installing.html). Similar to how we
use the PyTorch APIs we can use the C++ frontend and also support similar high level
APIs to interact with the Tensors. This library gives the flexibility of creating our
model in PyTorch and then for production we can move it to a C++ environment ( If it’s necessary ).

> C++ pipeline gives close to 3x or faster inference performance compared to PyTorch
> version.


### What's TorchScript

A serialized Model representation that can be used to export the models trained in 
PyTorch and run it on any other place without python dependencies. for eg; if you
can create a TorchScript version of your model, it can be loaded into Python or
C++ or other languages that have libtorch support.

Tensorflow employes the protocol buffer based serialization standards to ensure the
model representations are kept in the given format.

> TorchScript has a restricted python syntax, and it compiles this python code into the
> intermediate interpretable format. Like a small Virtual Machine, which produces the
> TorchScript that can be run on any torch runtime; ie; it can be on standalone C++
> program or with python itself.

For a more detailed introduction please check the torchscript documentation, which explains
it in many details and an easy fashion.

> I wish Tensorflow has similar documentation as the PyTorch. The way PyTorch internals
> are organized and documented are very easy to follow as nothing different from how a 
> standard C++ program behaviors and python extension mechanisms


### Export the Trained Models into TorchScript

If you are familiar with PyTorch, it also behaves similar to the tensorflow graph
based execution but we aren’t handling any graph construction APIs. Instead, PyTorch
creates the Tensor operations as a graph dynamically when it sees python statements
that do some operations on a Tensor. For example, adding two tensors, and then the
next line does apply a nonlinear function on top of it. In Tensorflow the library
“Keras” does the dynamic graph construction hidden from the main APIs.

When we come to the generation of Torchscript representations of your model, you can do that in two ways, 

#### 1. Tracing

As the name suggests, the tracing method is used to record the set of operations for
a given input and export it as the torchscript representation of the model.

```python
detr  = <Instantiate DETR Model, a nn.Module class.>
img = Image.open("image.png").convert("RGB")

# Apply preprocessing and convert the image into a Tensor format with batch index.
im = transform(img).unsqueeze(0)

# Here we are doing inference on the “detr” model, meanwhile, the trace captures
# the Tensor operations associated with this inference in a Graph format.
detr_trace_module = torch.jit.trace(detr, im, strict=False)

# Save the torchscript model, that can be loaded in python or non-python
# environments.
detr_trace_module.save("detr_trace.pt")

# Load the torchscript model
ts_detr_model = torch.jit.load("detr_trace.pt")
```


#### 2. Script

Script (`torch.jit.script`) method tries to capture all the control flows in (restricted)
python code into the torchscript compatible representation. This captures full
operations that have been done on top of a given Tensor. Internally script parses the
restricted version of python and generates intermediate representations ( like java class files ).
The torchscript jit compiler can do this on the fly or this intermediate version can be
exported to the torchscript serialized representation.

```python
detr_tscript = torch.jit.script(detr)

# script won’t need any input, as it’s capturing the entire source code associated with the
# given class. We have ensured the implementation using only the standard python
# constructs supported by the torchscript jit compiler.

# Once the torchscript intermediate representation is ready, the process is similar to 
# the trace method.
```

I would recommend reading the PyTorch documentation, which explains these concepts better than mine - https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html

Here is the notebook to play with this on a DETR model with pic2card pipeline - [Ipython Notebook](https://github.com/microsoft/AdaptiveCards/blob/main/source/pic2card/notebooks/DETR.ipynb)

> TorchScript jit compilers provide a VM based intermediate representation of a model,
> and these representations can then be optimized using custom compiler optimization.
> Also this common representation can be exported to machine executable codes,
> specific to the particular chipset or similar custom platforms if needed.

This idea of treating the model as a graph of tensor operations ( or general programs ) and having a compiler stack that can parse and generate target executable codes seem pretty much reusing the concepts of the standard programming environment. Which makes it much easier to understand these problems as it’s similar to a normal java / C program!


####  C++ code snippet to load the detr torchscript model

```cpp

#include <torch/extension.h>
#include <torch/script.h>
// Other includes if any.


struct Detr
{

    std::string model_path;
    torch::jit::script::Module model;

    Detr(const std::string &model_path) : model_path(model_path)
    {
        loadModel();
    }

    const std::string &getModelPath()
    {
        return model_path;
    }

    void loadModel()
    {
        model = torch::jit::load(model_path);
    }

    // Other plumping and inference code follows.

}


```


For the full version of the above code, please refer to the pic2card [detr_cpp](https://github.com/microsoft/AdaptiveCards/blob/main/source/pic2card/mystique/models/pth/detr_cpp)
subproject. It includes a way to call this c++ inference pipeline from python
bypassing the inputs as `NumPy` to the c++ program. We have type casting options
to convert the NumPy representation into `cv::Mat` and from there to `torch::Tensor`
type. Directly converting from NumPy to torch Tensor seems tricky due to the
different memory layout of both tensor implementations. In case of `cv::Mat` to
`torch::Tensor` it’s pretty straightforward.


### Inference Speed gain

From our empirical experiment on the `DETR` based model, we have found that --
you can expect 3x or more speed gain compared to the PyTorch inference pipeline.
In our experiment, this comparison is done between PyTorch based model inference and
libtorch based model inference provided some part of the image pre-processing was
still in python itself.


### References

1. Pytorch Internals, [1](https://pytorch.org/blog/a-tour-of-pytorch-internals-1/), [2](https://pytorch.org/blog/a-tour-of-pytorch-internals-2)
2. [Detr CPP inference implementation](https://github.com/microsoft/AdaptiveCards/blob/main/source/pic2card/mystique/models/pth/detr_cpp)