Some Programming Strategies
===========================
:category: blog
:date: 26-01-2013
:title: Some Programming Strategies


Here I want to share some of my thoughts that helps me to make good decisions in
every point of my programming life. This might looks like obvious to some but
it was not in real life.

The code samples are in Python, But concepts are applicable to most of the
programming languages.

1. Use of Exception Handler and if-else statement
--------------------------------------------------

While writing a program we have to make sure that it won't fail for the edge
cases. So usually what most of them do is -- put a `if` condition to check for
such scenarios. When the program runs, it has to check these conditions every time
to make sure that it was not the special case. If your language
has Exception handling system -- you can make use of it to handle the edge
cases.

C doesn't have an exception handling system. It relay on error codes to notify the
calling function about what happens to the call. It returns 0 for a successful call or
a positive number, which represents an error. So the calling function has
to check for return code using `if-else` condition. There is no other option out
there.

But for those languages which has Exception handling system, we can make use of
it. But in that case we may mix up both if-else and Exception handling systems
to handle errors or edge cases.


**A Simple example** :-

Consider a daemonizing program, which check for pid file while starting/stopping.
It calls the bellow function to get the pid. The calling function has main
exception handler to make sure that its logic won't break.

When the bellow function got called - 

1. While starting the daemon program
2. While stopping the daemon program.


What does the main daemon program do in each case -

* **While starting.**
   a. If it found the pid file, it means the daemon is running. Program
      stops by saying another instance of same program is running. 

   b. If it gets an error while reading the file, then there was no pid file, so
      the program is not running (An exception might happen while reading the pid
      file). Create new pid file and start the program.

* **While Stopping.**
   a. If it found the pid file, remove it before stopping the program.

   b. If it didn't find the pid file, what it will do ?. It means there is no
   daemon running. Just report that to user.

Bellow mentioned are the code block that gets called by the main daemon
program to get the pid. See how we can handle the exceptions or errors using
Exception handler and/or if-else statement.

**Method 1**

.. code-block:: python
    

    # This is bad way of using exceptions, kinda defensive programming.
    def read_pid_file():
        try:
            f = open('daemon.pid', 'r')
            pid = int(f.read())
            return pid

        # No file in the path, may be other IO error.
        except IOError:
            raise "Faild to Read file"

        # Somebody put non integer values in the pid file. Whom to blame ?
        except ValueError:
            raise WrongPID

        # This catch all exception not necessarily required 
        # Since the calling function or main code has it. This is like
        # over use of exception handler feature.
        except Exception:                                    
            raise SomeUnKnownError

**Method 2**

.. code-block:: python

     # Using If/else method. The calling function has to check for None return
     # value or an Exception case.

     def read_pid_file():
         if os.path.exists('daemon.pid'):
             try:
                 f = open('file.pid', 'r')
                 # The programming languages which support exceptions
                 # internally  raises exception when it fails one operation.
                 # So we can't expect C like behaviour here.
                 return int(f.read())
             except (ValueError, IOError):
                 pass

**Method 3**

.. code-block:: python

     # Actually we know what going to happen, if some error happen while
     # reading the pid file, it gets handled by the calling functions' exception
     # handler. We are dealing with programming
     # language which has Exception handling system. So make use of it
     # effectively.

     def read_pid_file():
         f = open('daemon.pid', 'r')
         return int(f.read())
                 
I like the  **Method 3**, since it works for most of the time. It fail
rarely and at that time exception handler in the calling function should handle
it and decide its logic based on it. I'm not considering the edge cases due to race
conditions, since it was not for a real-time system :).
                

We know that both are important tools to make better good error free programs.

**When we use if-else statement**
    1. We know for certain what going to happen. Even though there are chance for
       different cases. ( C Error code mechanism is the good example ).

    2. We use if-else commonly to control the flow of the execution based on the
       input. 

**When we use Exeption handler**
    1. If we want to handle an error, otherwise leave it to system if you don't want
       to handle errors happened on your code. Those programming languages  which support
       Exceptions -- handles the exception itself on top level and report
       that to user unless you want your own way of error reporting.


2. Code Optimization
--------------------

Find out main code paths -- most of the time your program going to execute those
sections. Try to optimize those portions first -- that also not in the first
iteration of implementation. There should be remaining codes that handles edge
cases or Failure/Error cases, those portions not necessarily being optimized till
they are making any considerable noise on the performance :).


3. Number of lines of code.
---------------------------

Don't try to reduce number of line of code, instead reduce number of lines
of code per one job/task. Write simple functions/methods that do only
one job not multiple jobs, otherwise you may have good reason to do it.

**EDIT:** 05/Feb/2013

This may violate the DRY ( Don't repeat yourself ) principle, but there is
a good reason for it.

People usually try to reduce the number of lines by doing lot of jobs in single
code block and make the program  more complex,  and such code blocks has to 
maintain pre-requirements for all the different cases, in which most of the 
time one of those case may going to happen. So all extra work done there would cost
us when it executes.


4. Learn More about Operating System and Compilers
--------------------------------------------------
Understand the machine and try to understand how things are happening deep
inside the machine. That would be very useful to understand different bottle
neck cases. And it would help you to find out reasons for why strange things are
happening while running your code. 


5. Apply basic Management skills
--------------------------------

Apply Management skills to your programming. Pick right tool for right purpose
and think that way. I'm not 100% unbiased, but I'm working on it.


6. Chuck all rules described above :).
---------------------------------------

It happens some time!, and it's not a bad thing though. We do programs that way 
-- when we develop a new prototype or finding a solution for a particular issue, where
how we are going to implement doesn't make any importance but when we are
going to finish it does make. I think most of them might have gone through
such situations. For sure the good programming practices comes behind it.



Let me know your views about these points through comment. 

Reference :

1. https://stackoverflow.com/questions/328976/thorough-use-of-if-statements-or-try-catch-blocks
2. https://eli.thegreenplace.net/2008/08/21/robust-exception-handling/
