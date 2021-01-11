Title: Pytorch model inference in C++
Date: 2020-12-15  00:00
Category: data-science
Tags: pytroch,cpp
Authors: Haridas N

# Packaging Object Detection Models via Docker

Recently got chance to be part of an opensource effort from our [company](Imaginea) named pic2card. There we are mainly exploiting the object detection models for our usecase. Object Detection models become one of the main stream in the ML world, lot of innovative models came into existance recent years. Currently most of the models are trying to reduce the latency by keep the quality of the existing model, so that these can be applied for videos and realtime video streams. And this usecase is the one of the prime inputs for the self-driving application.

If you consider the different implementations avilable for the object detection you can see lot of implementations availble for the key architectures in tensorflow and Torch done against the main benchmark dataset named COCO, similar to the ImageNet datset for the Image competitions.


### how to structure the dependencies


### Master Dockerfile

The Multi-build feature of the docker helps to agregate the different control-flows with in the docker.

for eg;

1. I want to create docker file with model embedded in it.
2. I want to Keep the model as external service, so I don't need to install all the model specific heavy dependencies with my service.
3. Easy way to switch between these settings via environment variables.




Recently I was playing around on a object detection models specifically DETR model for one of the opensource project that we are working ( AdaptiveCards ).

DETR model implementation is using pytorch, as our pipeline is implemented is in python, was thinking of how we can deploy this library without using the pytorch and torchvision library.

You can easily develop models and networks using pytorch and at inference time you can use the torch.

Different implementations are available from Tensorflow and pytorch. The tensorflow library has more mature pipeline since tf-1.x version, and it's supported for the tf-2x version also. Pytorch side, things are moving very fast and more bleeding edge implementations of latest paper's are available, for eg; DETR

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

# Pytorch model Inference pipeline using c++

After seeing the option that we can easily move our model into C++ inference model, I couldn't wait to try this out with one of the Pytorch work that got into production environment. I have able to pack the entire model inference pipeline in C++, and export the C++ model via python wraper so that I can use the C++ inference pipeline in a another python only projects where i don't need to install the pytorch library specifically.

You can see the implementation of the c++ python package here:


Trying out the pic2card inference pipeline on the c++ library only inference option. The objectives are,

1. Reduce the net image size of the ML service
2. Reduce the latency as much as possible
3. CPP based python binding
4. Or use it with CPP projects directly

Currently these optimisations are possible using the pytorch environment using the the torchscript option.
