RabbitChat - Web based chat system
##################################
:date: 2011-07-28 12:10
:category: blog
:tags: programming,python,Server Architecture


**RabbitChat** is a simple Web based chat system developed in Tornado
Hight speed Python web framework. It uses Websoket for Full-duplex
communication over http and RabbitMQ Broker for message transaction
between server and connected clients.



.. figure:: /images/RabbitChat-Arch.png
    :width: 100% 

    If you want to try this now, checkout a copy of project from this
    github url `git@github.com:haridas/RabbitChat.git`. Or download it
    directly from `https://github.com/haridas/RabbitChat`_. Please check
    the README file for instructions about how to setup and run the
    application. It has one branch also, I explained the difference in
    README.


I tired to develop this same scenario in the gevent/twisted python
frameworks, but it lacks the support for good RabbitMQ clients. So after
long search I got an idea about how to implement this web based chat
system using Tornado Web Framework. I chose this because the python
RabbitMQ client Pika has good support for the tornado IOLoop, so that we
can integrate the RabbitMQ client with our web application and include
the WebSocket support easily.

I found few other web based Chat implementations on Gevent, but they
are not using the RabbitMQ for the message passing instead they relay up
on simple data structures. But I want this should be a RabbitMQ. Another
important thing was I want to use Websocket, all frameworks like Gevent
or Twisted or Tornado has support for websocket. But in this case we
need RabbitMQ client support also. Pika is the good python RabbitMQ
client, it has different adapters to integrate it with RabbitMQ and
other frameworks. Adapter for Tornado is already there, so that makes
this implementation possible. The Pika adapters for other frameworks
will come soon.

You may ask another question, why using RabbitMQ instead of a simple
Message passing data structures, Actually this application is a demo app
and I want to test the use of Websoxket with RabbitMQ. I'm looking
forward to develop a Realtime API's using this architectures. Google app
engine or other similar platforms( `Typhoonae`_) using Websocket server
similar to this way. So you can also develop a good implementations
using this demo application.

I hope this demo application helps you to get an idea about Real Time
Web application development.


.. _`https://github.com/haridas/RabbitChat`: https://github.com/haridas/RabbitChat
.. _Typhoonae: https://code.google.com/p/typhoonae/
