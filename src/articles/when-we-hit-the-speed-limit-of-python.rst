What happens when we hit the speed limit of python
==================================================


This post is not for braging python's problems, we know the limitations of the
python compared with compiled language. So here I'm explaining the scenario
where python was not the ideal choice.

We are using python for network programming, specifically a TCP client
which read packets from a C based server. We picked python because we
were already using it for other projects so more comfortable with it, and the
requirements at that point wasn't huge to condier compiled lanuges like C/C++
or Java.

So after installation in the client side, it was running without any problem
for more than an year. Then python cilent started to get socket exceptions
like,

    1. Errno: 104 - Peer closed the socket connection.
    2. Errno: 107 - Transport endpoint closed.


We initaliy thought this was happening because of python's long running process
exiting due to memory overflow or some other reason. We thought this because 
python's reputation as a long running deamon is not good. Then we figure
out that long running deamon wasn't the reason for this issue, since the main
python process wasn't consuming more RAM and it's very stable in memory usage.
Our python client using very simple data structures, so python VM very
efficiently handles the Memory.

Then I started to look into other areas of program, by changing the settings
and tuning prameters to see any of the fixing the issue. All of the options
seems to work for a while and exits some point in the future as before. I hit
a great wall and no idea about the issue and spend around a week to go throught
the program's in and out to see any possible causes. But all in waile.

Finally SO came into help, IRC wasn't helpful for these type of very specific
issue. Programmers can't live without Google and Stack Overflow. I put the
qustion on the SO, people helped me to make the question better for others by
adding the TCP traces picked up using ``tcpdump``. I got the expected answer
with in few hours.

Here is the link to the question - 

    I explained more technical details on the SO question, please have a look
    into it to know more details about the issue and test tcpdump trace file.

I'm very thankful to this guy. He went through the entire big TCP trace dump
and figure out the issue with the network traffic via TCP flags. Now it seems
pretty obvious that these are part of TCP flow control protocol.

The actual problem is the single threaded client which reading the data from
the socket, one thing we are right now not doing reading until socket is empty
due to some implementation restrictioins. We have to reduce the time taken to
handle one packet by the python proecss. Right now we moved out some of the
unwanted portions which delaying packet handling. After this changes now the
code is performing much better and no more socket related problems yet. Also
to handle the sudden traffic spikes we tweaked TCP output and input buffer
size to hold more packets in memory, so it will get cleared soon after things
are in expected speed range.

We are suspecious that the same problem will going to come in future, because
we have to match with the speed of the server. So right
now we are focussing on re-writing some of the core loops in C so it can match
with the server pushing speed.



I'm looking forward for more thoughts into these issues, please put your ideas
and suggestions via comments.


Until then,
Thank You.


