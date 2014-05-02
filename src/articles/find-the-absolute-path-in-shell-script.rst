Find the Absolute path in Shell Script
######################################
:date: 2011-11-19 06:01
:category: blog
:tags: server admin,shell

This is a simple shell script snippet to get the full absolute path of
that file while running it in a shell environment.

What is the use of this script -- Yeah, this script is really helpful
when you are looking for a stable deployment of a multi-file project in
a Unix based systems. For these type of deployments you have to deal
with the SYSTEM_PATH and PROJECT_HOME_DIR etc, to make our project run
properly by including relative files correctly from the system path.
Commonly what we do is, we hard code the SYSTEM PATH information to a
Global variable so that would resolve every relative path
properly. So how it would be, if we don't need to hard code the
Project Bases paths, instead the project configurations detect it
automatically :). So you could get this by using this shell script
snippet.

Here we can test how a shell script identify itself where it's located
or its absolute path information.Please create a shell script with
following content and run it from different locations.

.. code-block:: bash

 #Add this content in a shell.sh,
 #and then run it from different directory level, you can see the
 #difference.

 curr_dir=`pwd`

 dir=`dirname $0`
 FILE_PATH=`cd  $dir;pwd`

 echo "Path to this file : $FILE_PATH"

Add this script to **/usr/local/** and run it ( We know that
its current locations is **/usr/local/**)

.. code-block:: console

 # cd /
 #sh /usr/local/shell.sh
 Absolute PATH : /usr/local
 #cd /usr
 # sh local/shell.sh
 Absolute PATH : /usr/local
 #cd local
 #sh shell.sh
 Absolute PATH : /usr/local

I hope the output of the script explained every thing. So you can use
it in your projects to detect the current path automatically. Hope you
enjoyed this hack.

sEE YOU NEXT TIME.
