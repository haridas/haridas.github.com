Apache Camel with Guice and Servlet Container (Part 1)
======================================================
:date: 2016-01-25
:category: blog
:tags: apache-camel, guice


Working on with Apache camel for API gateway was a good experience. Here I want
to share my experience with running the camel applicatioin on servlet
containers.

As we know that a Camel application has a single global camel context, which
keeps information the application. So the simple workflow goes like this,

1. Build the camel context with required settings.
2. Define the routes / endpoints and register it with the camel context.
3. Expose all the routes via standalone server or servlet containers like Tomcat
   or jetty.

A simple camel application is given bellow, 

1. Camel Context setup
----------------------

// Simple Camel context construction code.

Camel context keeps a common global registry to register all the elements gets
into the camel contexts, for eg; components, endpoints, processors and custom bean
classes etc.


2. Construct endpoint
---------------------

Separate route building.


3.How to run it standalone
--------------------------

To test the camel application runs fine usually maps it with camel context and
run.


4. Running it on servlet container
----------------------------------

When we think about production level deployment, we need better scalable
options, so servlet-container is best option out there. Now we have to expose
all the camel routes via servlet configuration.

Camel comes with a servlet class that can be used to expose all the routes
defined using "servlet" component exposed through it.

We are using one servlet, to expose multiple endpoints, usually olden days we
have one servlet per endpoint. Here the job of the route management and
processing is handled by the camel context itself.


5. Running it on OSGi platforms ( Next blog plan, continuation to this one 2)
-------------------------------------------------------------------------------
This will come on next blog, Deploy the routes independent to the base camel
contexxt.


6. Dockerize the application
----------------------------
pass

7. Clustering the application
-----------------------------
clustering multiple camel contexts
