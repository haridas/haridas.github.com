Python and OOM Killer
=====================

:category: blog
:tags: python,oom,celery
:date: 2014-10-04


Those who are working with python for few years might have encountered this
problem at least once. What happens is that python processes are getting killed by
the OS's Out Of Memory Killer. OOM Killer does this to
reclaim the memory for OS, since there is no enough RAM space available for the
critical OS operations. This OOM killer getting involved with python 
processes is not due ot python's problem but because of how the programmer 
using python to get their things done.

Python is a fully Object Oriented and Dynamically typed language. Python's internal
memory manager does lot of optimization to make the program run faster with
effective use of memory. Python providing lot of flexibility for the coder, all
these flexibility costs internally while running (runtime cost) the code. But Python tries to
optimize this cost as much as possible. Programmers who know about this won't
blame python for its lack of performance with memory management compared to
statically typed language.

A sneak peek into python memory manager
---------------------------------------

Python's memory manager keeps it's own pool of memory(Private heap) for python
objects and this pool of memory was claimed from the OS via raw `malloc` call at low level.
Python's memory manager abstract the `malloc` call and provides its own special
`malloc` method specifically for different types of python objects. Python won't
release the memory back to the OS when an object goes out of scope in python
program. Instead it keeps this memory for future reuse.

The python garbage collector does reclaim memory back into OS if it meet certain
criteria  - Please read this `article`_ for more information about python's
memory allocation policies.

.. _`article`: http://www.evanjones.ca/memoryallocator/


We won't come across this problem if our system has enough RAM and peak memory
usage of the program comes under the RAM size. We usually start worrying about the
python's memory problems once the OOM Killer starts terminating the process.
Immediate steps to solve this problem are, 

1. Optimize the python program by using generators where every possible.

2. Learn best python programming paradigms. Usually newbies get into this
   problem because of the bad coding practices.

3. Know how much memory needs for your application in peak time and add that much
   RAM or Increase the SWAP. Use of swap space may not be very good because it
   will reduce the performance of the program if program constantly swapping 
   data from RAM to Disk.



I have encountered this problem while working with long running python programs
with it's peak memory usage is very higher than the average memory usage.

With Celery
-----------

Celery is a very famous distributed job scheduler in python. Most of them are
using it for their asynchronous task executions and other complex scenarios. Those
who using celery for simple tasks wouldn't have faced the memory issue. But in
our case -- we use celery very heavily.

RabbitMQ is the AMQP Message queue; backbone to the celery.

In our case what happened was that, we call celery tasks with `kwargs` - which
holds very large objects with no defined structure. Celery passes this data
through rabbitmq's queue and deliver to the actual celery's job runner which
runs the task with given `kwargs`. Since the size of the `kwargs` was very high
and the structure varies each time the celery's main process keep on increase
its memory foot print. Obviously if we have enough RAM then we can handle the
peak memory requirement but this minimum RAM size wasn't affordable to us,
so we have to find solution to prevent celery's main process from acquiring lot of memory.

The solution for this problem is, use `kwargs` (or `message`) with fixed structure and
small in size. Only pass ids or indexes through the message so that the celery's
main process won't acquire more memory. And celery has option to kill its worker
processes and respawn after some time, you can make use of this also so that
the work processes also release all its memory after some time and starts fresh.

RabbitMQ also recommends to use message with smaller size so that we get better
performance out of the system. This doesn't mean rabbitmq can't handle large
messages. The smaller message size reduce the IO overload required for the
RabbitMQ.

I hope this brief explanation will help you to tackle similar problems. If you
have any questions or suggestion please put it on the comment section bellow.


References
----------

1. http://deeplearning.net/software/theano/tutorial/python-memory-management.html
2. http://www.evanjones.ca/memoryallocator/
3. http://arctrix.com/nas/python/gc/
4. https://docs.python.org/2/c-api/memory.html
