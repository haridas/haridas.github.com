Title: Packaging Object Detection Models via Docker
Date: 2020-12-15  00:00
Category: data-science
Tags: pytroch,cpp
Authors: Haridas N

Recently got chance to be part of an opensource effort from our [company](Imaginea) named pic2card. There we are mainly exploiting the object detection models for our usecase. Object Detection models become one of the main stream in the ML world, lot of innovative models came into existance recent years. Currently most of the models are trying to reduce the latency by keep the quality of the existing model, so that these can be applied for videos and realtime video streams. And this usecase is the one of the prime inputs for the self-driving application.

If you consider the different implementations avilable for the object detection you can see lot of implementations availble for the key architectures in tensorflow and Torch done against the main benchmark dataset named COCO, similar to the ImageNet datset for the Image competitions.

### How to structure the dependencies

#### Requirements setting

1. Common dependencies for your ml service and preprocessing pipeline in `requirements.txt` file
2. Model specific dependency in corresponding requirements files. for eg; `requirements-tensorflow.txt`, or `requirements-pytorch.txt`

#### Dockerfile

Dedicated Dockerfile for each type of pipeline, provided they have options to change the pipeline properties at image build time itself. Make use of the Multi-stage dockerfiles, which helps to build different types of docker images.

Tensorflow based models can have options like these

1. With model embedded
2. using TFS service
3. GPU based inference support - We have to install GPU specific tensorflow if it requires. Otherwise we could save close to 1GB of dependencies required for the tensorflow gpu package.

This is same for the Pytorch scenario also

1. Package the model as normal pytorch export
2. C++ Inference pipeline
3. With GPU or Not

## Master Dockerfile

The Multi-build feature of the docker helps to agregate the different control-flows with in the docker.

for eg;

1. I want to create docker file with model embedded in it.
2. I want to Keep the model as external service, so I don't need to install all the model specific heavy dependencies with my service.
3. Easy way to switch between these settings via environment variables.

## API Abstraction

UML diagram if possible.

So like many such tricks and tips from the standrd software engineering concepts can be applied to make the ML model deployment and management of the project much easier for long run to maintain and iterate the models quality intependent of the actual pipelines.

Hope this helps, to see all these explained in a single project please checkout the pic2card source code.

Some approaches from Tensorflow and Pytorch


| Features | Pytorch | Tensorflow |
| - | - | - |
| Model Export | Torchscript | frozen graph_def |
| Serving | Embed | Embed / TFS |
|   |   |   |

### Package size difference:


| Package | Size | Target |
| - | - | - |
| torch==1.6.0+cpu | 470MB | Linux |
| torchvision==0.7.0+cpu | 17MB | Linux |

Inference time difference:

### Model Size and its parameters size:-


| Model Name | #Params | float64 |
| - | - | - |
| Faster-RCNN: |   |   |
| DETE |   |   |
| EfficiendDet-0-7x: |   |   |

### Main stages involved

1. Create TorchScript representation of the model
2. Do the trace run to get python intenepndent representation, so that you can load them in libtorch library ie; cpp/c
3. CPP inserference library you can now directly load this torch script model.
4. Provide the inputs via cv::Mat or other compatible matrix format.
5. If you further want to load this cpp inference as a python binding to any other python projects that doesn't need explicit pytorch dependency, you can do that.
6. As the size of the torch library size is higher.

This is not a common pipeline but needed for high throughput systems where we need to integrate any ML-based solutions we have to package the model as a Linear Algebra module that does some vector calculations and produce the result as quick as possible.

1. Export your model to TorchScript Format
2. Load this model in CPP program.

Size comparison between libtorch and pytorch ?

---


Title: Pytorch model Inference pipeline using c++
Date: 2020-12-15  00:00
Category: data-science
Tags: pytroch,cpp
Authors: Haridas N

After seeing the option that we can easily move our model into C++ inference model, I couldn't wait to try this out with one of the Pytorch work that got into production environment. I have able to pack the entire model inference pipeline in C++, and export the C++ model via python wraper so that I can use the C++ inference pipeline in a another python only projects where i don't need to install the pytorch library specifically.

You can see the implementation of the c++ python package here:

Trying out the pic2card inference pipeline on the c++ library only inference option. The objectives are,

1. Reduce the net image size of the ML service
2. Reduce the latency as much as possible
3. CPP based python binding
4. Or use it with CPP projects directly

Currently these optimisations are possible using the pytorch environment using the the torchscript option.
