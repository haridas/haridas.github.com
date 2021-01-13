Title: Packaging Object Detection Models for Production
Date: 2020-12-15  00:00
Category: data-science
Tags: pytroch,tensorflow,docker
Authors: Haridas N

Recently I got chance to be part of an opensource effort from our [company](Imaginea) named pic2card. There we are mainly exploiting the object detection models for our usecase. Object Detection models become one of the main stream in the ML world, lot of innovative models came into existance recent years. Currently most of the models are trying to reduce the latency by keep the quality of the existing model, so that these can be applied for videos and realtime video streams. And this usecase is the one of the prime inputs for the self-driving application.

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

Right now we are targetted to do the CPU only inference on the cloud lambda services, in our case [Azure Functions](https://azure.microsoft.com/en-in/services/functions/). So to check how the tensorflow service being seutup, see below main docker file which handles the option to include the inference model with dockerfile or exclude and use the external service which does the actual model inference.

The Multi-build feature of the docker helps to agregate the different control-flows with in the docker.

for eg;

1. I want to create docker file with model embedded in it.
2. I want to Keep the model as external service, so I don't need to install all the model specific heavy dependencies with my service.
3. Easy way to switch between these settings via environment variables.

< Show sample of the docker file and its stages >

## API Abstraction

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

Docker Image Sizes:

Both images 1GB+ images, which makes it easy for deploy it on Serverless environments. We need to be strictily avoid all unncessary package installations to make this work.

### Github Actions Integration

This would be an Iceing on the cake feature for you, This helps to avoid all the headache of running the builds yourself, and it helps to avoid extra efforts that need to be put in to do the sam relase process after few months. As obviously most of the part of the pieline by then will be forgotten.

So Actions helsp to make the end-to-end pipeline works well, and error free and it's less streassful for the entire team.

### Github Docker Registry

This is another feature we get for free from github, if your project is a opensource one. You can build the images using github actions and keep them under the github docker registry. This makes the life easyer for build and keep the publically available images for anybody to deploy or try it out.

See the below action codes under the pic2card source code to know more about how to integrate the actions with github registry.

To see all these dicussed methods in action, checkout the opensource project named Pic2Card under AdaptiveCards framework - [https://github.com/microsoft/AdaptiveCards/tree/main/source/pic2card](https://github.com/microsoft/AdaptiveCards/tree/main/source/pic2card)

Github Actions available under the root of that project: [https://github.com/microsoft/AdaptiveCards/tree/main/.github/workflows](https://github.com/microsoft/AdaptiveCards/tree/main/.github/workflows)
