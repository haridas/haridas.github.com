What happens when we hit the speed limit of python
==================================================
:category: blog
:date: 10-04-2014
:tags: python,networking,tcp


Python is a beautiful language but we know the limitations of the
python compared with compiled language. So here I'm explaining a scenario
where python was not the ideal choice.

We are using python for network programming, specifically a TCP client/server
program which read packets from another C based server. We picked python because 
on the requirements the traffic volume wasn't huge enough to consider compiled
languages like C/C++ or Java, and we are already using python so more comfortable 
with it. 

The network topology
--------------------

.. code-block:: text

 Network => TCP Server A => TCP Server B ( Do some operation.) ==> Network

 Where :- 
     Server A is implemented in C.
     Server B is the one we implemented.

The data flowing from Server A to Server B via TCP. The Server B is implemented
in python for now. This setup was running for more than a year without any
problems or crashing. Then it started showing problems. The Server B crashing
sometime because of the socket connection between the Server A and Server
B getting closed by the Server A, We don't know why. Bellow listed are the errors
that we are getting, one interesting thing is; these two errors won't happen
together, some time Errno 104, some time Errno 107.


    1. Errno: 104 - Peer closed the socket connection.
    2. Errno: 107 - Transport endpoint closed.


I initially thought this was happening because of python's long running process
exiting due to memory overflow or some other reasons. We thought this because 
python's reputation as a long running daemon is not great. Then we figure
out that long running daemon wasn't the reason for this issue, since the main
python process wasn't consuming more RAM and it's very stable in memory usage.
Our python server using very simple data structures, so python VM very
efficiently handling the Memory.

Then I started to look into other areas of program, by changing the settings
and tuning parameters to see any of it fixes the issue. All of the options
seems to work for a while but it throws the same error after few days.
I was stuck and no idea about the issue and spend around a week to go through
the program's in and out to see any possible causes. But no clue from it.

Finally Stack Overflow came into help, IRC wasn't helpful for these type of very
specific issues. Programmers can't live without Google and Stack Overflow. 
I put the question on the SO, people helped me to make the question better by
adding the TCP traces picked up using ``tcpdump``. With in hours I got the 
answer I was looking for. It's mainly due the python socket reading related.
In the Python side we are not clearing the TCP packets from the receive buffer
of TCP socket completely, only reading few bytes (300B to 10KB) at a time.
So which causing the Python server to send receive window size flag of TCP
protocol as ZERO for multiple times In the heavy traffic period.
This might triggering this issue. That was the idea I got from the stack Overflow.

You can see the `stackOverflow post`_, I explained more technical
details on the SO question, please have a look on it to get more details about
the issue and sample tcpdump trace file to see what was happened on the network.

.. _`stackOverflow post`: http://stackoverflow.com/questions/22142730/tcp-connection-reset-by-peer-and-transport-end-point-is-not-connected


The problem on the python side is that,  it's a single threaded server which
reading the data from the socket, one thing we are right now not doing is reading 
until socket is empty due to some implementation restrictions. From the SO
answer I got some quick solutions to try, 

1. Remove unwanted codes from the main loop, so the total time taken to process
   one socket read would be as small as possible.
2. Tweak with the Kernel parameters for the TCP sending and receiving buffer
   size.
3. Improve the Code base or re-implement it in C completely or do the main part as
   C extension.


The method 1 and 2 was easy go ahead with, So I did it right away. It gives
considerable difference and the crashes reduced considerably. But still it
happened once or twice. So I know that it's not enough and need reimplementation
of the parts which causing this problem. But we are holding  on the
reimplementation since it will take lot of time to change the existing stuff.
Any way the current changes give enough time to try more things to improve the
existing code and investigate the problem more.


Mean while I did some more investigation locally to understand the issue more.
From that what I understood was, when the network is heavily loaded the Python
server side not clearing the traffic quick enough and which forcing the remote server
to close the TCP socket (Not yet found why it's closing it). Right after the
socket is closed on the remote end,  Python side of the code might be trying
`socket.send` or `socket.recv` and it will fail since no active socket. So in
the beginning I mentioned that I'm getting two errors, this is
because some time right after the remote server closed the socket, the next
socket interaction in the python side may be `socket.send` which was triggering the
error ``Errno 104``. If it was `socket.recv` it would have been ``Errno 107``. 
 
 
One other thing I learned after this was that, the TCP server usually handles
the slow remote servers by blocking the new massage write into
the sending buffer. In my environment I understood the remote server A 
is not blocking the write(Non-blocking socket) instead closing the socket( This
could be due to timeout).If the TCP server has option to cache the extra
packets into disk then it could have handled this peak traffic period.

A TCP Server has to provide atleast these features
---------------------------------------------------

1. Way to handle the buffer overflow if the client is very slow.

2. Write the buffer overflowed data into durable queue or file system.

3. When the Client comes back, the server has to automatically deliver the
   pending messages in FIFO order.


Final thoughts
--------------

If these options are there with the TCP server that I was handling, this problem
couldn't have happened. So finally now I can say that Python
could have handled this situation if the traffic spikes some times only - In
our case that was the situation. Python couldn't have done it if the rate of
server is more than the rate at which Python can clear the socket backlog.


references
----------

1. http://linux.die.net/man/2/sendmsg 
2. $ man socket

