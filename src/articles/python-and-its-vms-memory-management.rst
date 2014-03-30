Python and Its VM's memory management
=====================================
:date: 
:tags: blog
:tags: python,vm,memory



We are fed up with the python process which won't release the memory after
usage back to the OS, instead keep it for future usage. This optimization
behaviour by the python VM's Memory manager causing Out of Memory killer to
kill some other process which are relevent.


This was happening with our celery the distributed parallel processing package.
Our product currenlty using celery heavely to do the real tasks. Because of
these tasks are long running and very memory intensive at times, we were facing
the problem of the Over memory killer to reclaime some of the memory from some
process.


We know that the celery's main process is very stable and has no memory leak
reported. Unless we were sending very complex and hetrogenious data structures
into it. We are using rabbitmq as our broker, and we sends the message with
huge size controry to the recommended small size message for better performence
of the celery main process.



