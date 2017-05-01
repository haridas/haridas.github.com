What I Like about J2EE
======================

:date: 2016-07-25
:category: blogs
:tags: j2ee,java8


I started with J2EE coding very late after coding for 6 years mainly in python
and other languages like Nodejs, c++, go, c# etc. As a late starter I happy that  I got
chance to work with the latest technologies in SOA environment. From that experience
I just want to put down some points that I liked about java, as I'm coming
from other languages I felt few things are interesting to me.

Interfaces 
----------

As a Object oriented language it doesn't have multiple inheritance, but it
provides Interfaces. If you check java libraries there are lot of standard
interfaces reused from Java language. Also J2EE provides lot of standard
interfaces to the application or product developers to come up with their on
implementation.

May be key example for this would be the Servlet interface in J2EE. If you see Servlet
containers(Jetty, Tomcat), it comes with its own implementation of the 
`HttpServletRequest` and `HttpServletResponse`, all these implementation follows
standard interface given by the J2EE. What it means is we develop our application
independent of servlet container implementation or we can run the web application
on any servlet container as it should be.

Interfaces are good for more disciplined and consistent software development.
I think the current Oracle vs Google fight is because of this standard interfaces.
Google doesn't want to change the interface to make it look like another cousin
language.

Standards
---------

Most of the mainstream languages got their own feature addition process to 
propose feature requests for the language. For java it called JSR ( Java
Specification Request). Here goes all the initial design proposals and drafting
of the specification and mostly it follows a reference implementation of the new specification.
I'm curious to see the final implementation of following JSR, and other interesting JSRs.

`JSR-369`_: Servlet 4.0 with http2 support ( Under review stage)

`JSR-311`_: JAX-RS Java Restful web service specification. Reference
implementation `Jersy`_

`JSR-370`_: JAX-RS 2.1 New specification to get HTTP2, non blocking I/O and etc.
            This will really make the JAX-RS more powerful and widespread.

`JSR-330`_: Defines the standard annotations for dependency injection, @Inject, @Named,
@Provider, @Singleton and @Qualifier and how it should behave.

`JSR-229`_: J2EE standard Dependency injection engine, supports the JSR-330
convention.

.. _`JSR-369`: https://www.jcp.org/en/jsr/detail?id=369
.. _`JSR-311`: https://www.jcp.org/en/jsr/detail?id=311
.. _`JSR-370`: https://www.jcp.org/en/jsr/detail?id=370
.. _`JSR-330`: https://www.jcp.org/en/jsr/detail?id=330
.. _`JSR-229`: https://www.jcp.org/en/jsr/detail?id=229
.. _`Jersy`: https://jersey.java.net/

Servlets, servlet filters and web-fragment for Micro service development
------------------------------------------------------------------------
I got surprised by the flexibility of these standard interfaces supplied by the
J2EE. It's more than enough to develop a web service or web framework from the
ground up without much boiler plate codes. Assume if you want to do some request
response validation via swagger schema, it's much simple by adding a servlet
filter for it and wrapper classes to intercept the response stream.

I worked with MVC frameworks which uses a concept called middleware to intercept the
request/response flow before actual processing, I felt the servlet filter acts the same role
in J2EE platform. I agree the fact that J2EE is a Java plus lot of libraries, may
be we can consider it as a web framework :).

Usually to package the servlets and filters, there is web.xml file, it
does the url routing logic, and the filter ordering, this is kinda configuration
files in different frameworks, but it's in xml ;).

Another interesting thing is `web-fragment.xml`_. This is really good feature
which we leveraged to build a micro web framework with default routes ( /admin,
/health, /doc etc) and supplied to developers as jar file. You can call this as
a micro web framework which can be used in the micro service development
environment where the number of routes in a particular service going to be very
minimal.

.. _`web-fragment.xml`: http://www.oracle.com/technetwork/articles/javaee/javaee6overview-part2-136353.html


Dependency Injection
--------------------

DI was the one area I spend most of my time. I integrated libraries which comes with
DI support into our application. Mainly I used google guice because those
libraries already implemented in google guice DI so we didn't have much choice.

The thing I liked about the DI is its magics. How it wire the actual
implementation classes to the interfaces. There are standard set of annotations
defined for DI purpose, `JSR-330`_ defines it, You can import it from the
package `javax.inject`_. Currently most of the DI
implementations supports JSR-330, and it's recommended to stick to JSR-330 while
using injections in our code so that we can easily switch the actual DI engine
based on application requirements.

As described above `JSR-330`_ defines the annotations that can be used to tag the
injection behavior across the code. Google guice, CDI, and Dagger are the few
famous Dependency Injection library. In which CDI is the standard implementation comes
with J2EE and described in `JSR-229`_. Looks like most of the servlet containers
are now support CDI by default. But I felt like CDI is bit more
magic than google guice. Google guice does the manual bindings by default and
it's more explicitly but CDI does the auto scan across the class path to find
the implementations and targets on which it can be injected.

I will stick to google guice if third party libraries are already making use of
it, if that's not your case then, going with CDI is best for the future support and platform
compatibility across J2EE environment.

.. _`javax.inject`: http://docs.oracle.com/javaee/6/api/javax/inject/package-summary.html


Unit Testing and Logging libraries
----------------------------------
One of my favorite libraries in Java. New annotation based Test methods are
far easier to write. The test runner automatically knows the Test classes and
test methods. You can test each and very part of your application using
Junit and some mocking library. We tested entire micro service from the
servelet filter level.

Logging library got much more flexibility, and python's logging library was
designed after this one. I liked the design of `slf4j`_ how easily we can
configure the backends and its logging behaviors via xml configurations. Slf4j
is the another example of standard Interface which keeps the logging API common
across multiple logging frameworks ( log4j, logback and java.util.logging).

.. _`slf4j`: http://www.slf4j.org/

Servlet Containers and OSGi
---------------------------

There are lot of of servlet container implementations exists,
famous one are Jetty and Tomcat. Jetty is small and more easy to embedded
in your code. Most of the servlet containers are do auto reload if we place the
war files into its ROOT folder.

Apart from the standard servlet containers, I liked the concept of `OSGi`_. OSGi is
more modular and service oriented platform. You can release you project as jar
file with some version details ( As the standard jar doesn't have any notion of
version). We can expose our application interfaces as services to
other teams, they can consume it easily. I tried few POCs with the `apache
karaf`_ and `karaf celler`_ to know more of it.

.. _`OSGi`: https://www.osgi.org/

I felt OSGi gives all the tools required to go with SOA based microservice
application development. Apache karaf team call their platform as polymorphic
container it can run OSGi bundles, war, jar, spring etc.

.. _`apache karaf`: http://karaf.apache.org/index.html
.. _`karaf celler`: http://karaf.apache.org/projects.html#cellar

Java community
--------------

Java community is huge and vast with around 2 decades of experience and maturity
in the tools and platforms build on it. And the new language upgrades catching
up with the new trends in computer language arena.  eg: Java8 got lambdas,
functional stream processing APIs etc. And interestingly java9 comes with a REPL.

Conclusion
----------

People who says about java is verbose and rigid compared to 
other languages. But I would say that verbosity thing can be easily overcome
by using a good IDE. Regarding the flexibility it's purely with the product
design. I mostly see development flows like this, develop the initial product using any of
the language that you are comfortable with, if the situation arises for more scalability / 
reliability / speed you can switch to java or other static languages.
If you consider the SOA platforms this isn't required at all, create your
microservice using the tool or language which fits best on top of a standard
communication protocol ( http / thrift / protocol buffer etc ).

References:-
------------
1. `Oracle and Fall of J2EE`_
   
.. _`Oracle and Fall of J2EE`: https://techsticles.blogspot.in/2016/07/oracle-and-fall-of-java-ee.html?utm_content=bufferf1a2e&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer
