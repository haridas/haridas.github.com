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

Update (02-May-2014):-

Please check out this `reddit`_ discussion about this post, which give you more
insight into the problem and possible solutions.

.. _`reddit`: http://www.reddit.com/r/Python/comments/24jaxr/what_happens_when_we_hit_the_speed_limit_of_python/#ch7rd9y

Update ( 03-May-2014):-

Simulate the Production Environment
-----------------------------------

So finally I got the working sample to simulate my server and client
behaviour. This was only possible from the encouragement I got from reddit and
twitter for my this blog entry. Thank you guys.

Here I created one C tcp sample server(tcp_server.c), which simulate my actual C
server in the production environment. And one Python TCP client(tcp_server.py) 
which simulate the TCP socket reading operation in the production Python server
implementation.

.. code-block:: python
    
    # Python server tcp_server.py 

    from optparse import OptionParser
    import socket
    import time
    import select

    PORT = 8000
    HOST = "localhost"


    def start_tcp_client():
        """
        Connect to sever and push lot of data.
        """
        print "Starting Client"
        sock = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((HOST, PORT))

        count = 1
        while 1:
            print "sending " + str(count)
            data = sock.recv(10)

            #
            # Does some action on the data. and return the response.
            #
            time.sleep(0.5)

            sock.send('Hi i got the data')
            print data
            count += 1


    def start_tcp_client_with_fix():
        """
        The TCP client with fix applied. So it will read complete data from socket
        and avoid the errors like 'errno 104' or 'errno 107'.
        """
        print "Starting the newly implemented client..."
        sock = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((HOST, PORT))

        # make the socket non-blocking
        sock.setblocking(0)

        count = 1
        while 1:
            print "sending " + str(count)
            data = ""
            t_data = ""

            rsock, _, _ = select.select([sock], [], [])
            if rsock:
                rsock = rsock[0]
                try:
                    while(1):
                        t_data = rsock.recv(1024)
                        data += t_data
                except Exception as ex:
                    if ex.errno == 11:  # EAGAIN
                        # Nothing more to read;
                        pass
                    else:
                        raise ex
            else:
                continue
            #
            # Doese some action on the package `data`
            #
            print "Handled {} bytes".format(len(data))
            rsock.send(str(len(data)))

            count += 1

    if __name__ == "__main__":

        parser = OptionParser()

        parser.add_option("-c", "--client", action="store_true",
                          dest="new_client",
                          default=False,
                          help="Start the new client with fix applied.")

        options, args = parser.parse_args()
        new_client = options.new_client

        if new_client:
            start_tcp_client_with_fix()
        else:
            start_tcp_client()



.. code-block:: cpp

    /*
        tcp_server.c - Implements the TCP server in my production environment.
    */

    #include <stdio.h>
    #include <stdlib.h>
    #include <stdlib.h>
    #include <string.h>
    #include <unistd.h>
    #include <errno.h>

    #include <netdb.h>
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <arpa/inet.h>
    #include <netinet/in.h>
    #include <sys/wait.h>
    #include <fcntl.h>


    #define PORT "8000"
    #define HOST "127.0.0.1"
    #define MAX_LISTEN 5
    #define SIZE 512


    void *get_in_addr(struct sockaddr *sa){
        if(sa->sa_family == AF_INET){
            return &(((struct sockaddr_in*)sa)->sin_addr);
        }

        return &(((struct sockaddr_in6*)sa)->sin6_addr);
    }


    int send_sock_msg(int sock_fd){
        struct sockaddr_in receiver_addr;

        char line[15] = "Hello World!";
        struct msghdr msg;
        struct iovec iov;

        //sock_fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

        receiver_addr.sin_family = AF_INET;
        receiver_addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
        receiver_addr.sin_port = htons(8000);
        
        msg.msg_name = &receiver_addr;
        msg.msg_namelen = sizeof(receiver_addr);
        msg.msg_iov = &iov;
        msg.msg_iovlen = 1;
        msg.msg_iov->iov_base = line;
        msg.msg_iov->iov_len = 13;
        msg.msg_control = 0;
        msg.msg_controllen = 0;
        msg.msg_flags = 0;

        return sendmsg(sock_fd, &msg, 0);
    }

    int main(void){

        int sd, new_sd;
        int yes = 1;
        int rv;
        int ttl = 8;
        char s[INET6_ADDRSTRLEN];

        struct sockaddr_in addr;
        struct addrinfo hints, *serverinfo, *p;
        struct sockaddr_storage their_addr; // COnnectors address info.
        socklen_t sin_size;

        memset(&hints, 0, sizeof(hints));
        hints.ai_family = AF_UNSPEC;
        hints.ai_socktype = SOCK_STREAM;
        hints.ai_flags = AI_PASSIVE;

        if((rv = getaddrinfo(NULL, PORT, &hints, &serverinfo)) != 0){
            fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(rv));
            return 1;
        }

        // Loop through different results and pick up the first one.
        for( p = serverinfo; p != NULL; p = p->ai_next){

            if ((sd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
                perror("server: socket");
                continue;
            }

            if((fcntl(sd, F_SETFL, O_NONBLOCK)) < 0){
                perror("error:fnctl");
                exit(EXIT_FAILURE);
            }

            if(setsockopt(sd, SOL_SOCKET, SO_REUSEADDR, &yes,
                        sizeof(int)) == -1){
                perror("setsockopt");
                exit(1);
            }

            if(bind(sd, p->ai_addr, p->ai_addrlen) == -1){
                close(sd);
                perror("server: bind");
                continue;
            }

            break;
        }

        if (p == NULL){
            fprintf(stderr, "server: failed to bind \n");
            return 2;
        }

        freeaddrinfo(serverinfo); // No need for it further.
        
        if(listen(sd, MAX_LISTEN) == -1){
            perror("listen");
            exit(1);
        }


        printf("server: waiting for connections...\n");

        while(1){
            sin_size = sizeof their_addr;
            new_sd  = accept(sd, (struct sockaddr *)&their_addr, &sin_size);

            if(new_sd == -1){
                perror("accept ...");
                sleep(1);
                continue;
            }

            inet_ntop(their_addr.ss_family,
                    get_in_addr((struct sockaddr *)&their_addr),
                    s, sizeof s);

            printf("server: got connection from %s \n", s);

            if(!fork()){ // This is child process.
                close(sd); // Child doesn't need the listner socket. I'm not sure thought.
                int count = 1;
                FILE *logfile = fopen("server.log", "w");

                if(logfile == NULL){
                    perror("logfile open error");
                    return(-1);
                }

                /*
                 * Change the new client socket non-blocking.
                 *
                 * This will simulte the server scenario by writing the send buffer
                 * as much as it can, and returns -1 if it's full. So that point the
                 * server is reset the connection by closing the socket.
                 *
                 * So that's the current server behaviour in my environment. Check
                 * the python client side, how it handling to avoid the connection
                 * reset by the server.
                 */
                if((fcntl(new_sd, F_SETFL, O_NONBLOCK)) < 0){
                    perror("error:fnctl");
                    exit(EXIT_FAILURE);
                }

                while(1){
                    int numbytes;

                    sleep(0.1);

                    if((numbytes = send_sock_msg(new_sd)) < 0){
                    fprintf(logfile, "Kernel sending buffer is full. Closing the connection.: %d %d\n", count,numbytes);
                    close(new_sd);
                    exit(EXIT_FAILURE);
                    }

                    fprintf(logfile, "Server sending the msg no: %d %d\n", count,numbytes);
                    count ++;
                }
                close(new_sd);
                exit(0);
            }

            close(new_sd); // Parent doesn't need child's socket.
        }

        return 0;
    }


How to Run the code.
--------------------

.. code-block:: bash

    #
    # Start the C server. Which listening on the port 8000 and handles the
    # Client connections on another thread.
    #

    $ gcc tcp_server.c
    $ ./a.out

    # 
    # On another shell environemnt run python client.
    # It has two options - 

    #    1. Run the Python client which gives the error 104 and 107 issue. Which
    #       is the issue I'm getting right now on the production machine.

    #    2. Another implementation of the Python client which fixes the issue and 
    #       read the socket data without causing socket error 104 and 107

    $ python tcp_server.py  # Simulate the tcp client with socket problem.

    #    This will crash after while since the server closes the socket on its
    #    side due to the kernel sending buffer is full on the server side.

    $ python tcp_server.py -c # This client has the option to fix that issue.

    #    This will read the socket data in non-blocking mode and read entire 
    #    data from the socket till it throws EAGAIN exception.

    #    This time the client won't throw any excetion and the server and client
    #    work smoothly. So finally I got the protype to fix the actual production
    #    system.

    #    To See what is happening while running this scripts run `tcpdump`
    #    caommand.

    $ sudo tcpdump -i any port 8000



references
----------

1. http://linux.die.net/man/2/sendmsg 
2. $ man socket
