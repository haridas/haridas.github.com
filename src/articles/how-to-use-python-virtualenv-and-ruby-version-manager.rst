How to use Python Virtualenv and Ruby Version Manager
#####################################################
:date: 2011-08-31 06:20
:category: programming
:tags: python,ruby

First thing I want tell you that here I'm not comparing these two tools
instead only describing how to install and use them.

We use these tools to isolate the multiple Python or Ruby versions from
system default Python or Ruby installation. We use Virtualenv for Python
and RVM(Ruby Version Manager) for Ruby.

Let's consider, our server has slightly old version of packages but we
are currently working with latest version of Python or Ruby packages for
our project, then most probably our project package dependency might be
conflict with corresponding packages installed in the system default
path. To get this work, updating the system packages might not be a good
method, because it may broke our existing projects that depends up on
the system packages and it's very dangerous...!. This problem is common
now because of rapid development and feature updation of packages. To
solve this issues and use the packaging system more flexibly both Python
and Ruby providing their own tools.

We can first check the Python Virtualenv tool for python projects.

**Virtualenv**
--------------

Virtualenv package isolate python package system and corresponding
binaries in to a user defined folder.

First install `virtualenv` package by using default pythons package
installation tool or you can use `pip`.

.. code-block:: console

 #easy_install virtualenv


To create new virtual environment,

.. code-block:: console

 $virtualenv python_project


This command will create new folder 'python_project', inside this
folder we have three other folders 'bin' for python and other binaries ,
'include' for python header files and finally 'lib' folder holds all
python standard packages. When we will install new python packages under
this virtual environment those files also been comes under this lib
folder.

To activate and use this virtual environment,

.. code-block:: console

 $cd python_project
 $source ./bin/activate


Above command will change the current shell session by updating the
system PATH and it also change the shell prompt, to get a notion of we
are in the virtual environment.

.. code-block:: console

 (virtual)host@name$ which python
 PATH-to-DIR/python_project/bin/python
 (virtual)host@name$ which easy_install
 PATH-to-DIR/python_project/bin/easy_install

Now you can see that `python` and `easy_install` commands were from
our virtual environment. When creating a virtual environment the basic
python interpreter and package installation tools (`easy_install`
and `pip`) were created under the bin directory so you can directly
use them to install new packages under virtual environment easily that
never going to affect the python packages installed in the default
system path(/usr/lib/python-2.x/).

.. code-block:: console

 (virtual)host@name$ deactivate

This will deactivate our virtual environment and the control will be
return to system shell prompt, after removing all changes in the system
PATH variable.

So like this you can create any number of virtual environments with
different package installed in it depending on your project
requirements.

**UPDATE**
----------

There is another package 'virtualenvwrapper' to organize and use the
multiple virtual environments by single set of shell commands. Here is
the brief description about virtualenvwrapper.

To install virtualenvwrapper, as usual you can use easy_install or pip

.. code-block:: console

 #pip install virtualenvwrapper

After the installation append the following two lines to .bashrc or
.profile file.

.. code-block:: console

 export WORKON_HOME="~/.virtualenvs"
 source /usr/local/bin/virtualenvwrapper.sh

Now from next shell session onwards following commands would be
available to us, which helps to manage the multiple virtual
environments.

.. code-block:: console

 Create a new virtual environment and enter into it.

 $mkvirtualenv test_proj

 To deactiave
 $deactivate

 If we created multiple virtual environments, to list it by using,
 $workon

 To Activate particular virtual environment from above list.
 $workon

 To remove the virtual environment
 $rmvirtualenv

This package also provide PRE and POST hooks for all of its commands ,
we can use those hooks to inject our codes while running the
virtualenvwrapper commands.

This viritualenvwrapper is an additional package that really help both
administrators and programmers to manage multiple project environments
with different versions of python packages were installed.

Now take a look at how we can do the similar thing in Ruby ,

**Ruby Version Manager - RVM**
------------------------------

RVM tool handle multiple ruby versions (ruby-1.8.2, ruby-1.9.1,
ruby-1.9.2 etc..) in our system and help us change the version of ruby
in our system without affecting the ruby installed in our system default
path. for eg; by default our system have ruby-1.8.2 installed, but we
want ruby-1.9.2 for our project. So after installing the ruby-1.9.2
using `rvm` we can change system default ruby version to ruby-1.9.2,
we can revert this back to system ruby when we requires.

So in this manner we can install multiple ruby versions and switch
between them, once we switch to a particular version of ruby then that
ruby is available for that system user. This is the brief description
how RVM works in our system. Lets move to setup part.

You can install RVM from `root` (Multi user mode)user privilege or
from a `user` privilege(Single user mode). The single user mode were
recommended, because the RVM only avaiable to that user only, but in
Multi-user mode of RVM installation make it available to all users in
the system.Here we will install RVM in single user mode.

To install RVM you can use git if it available in your system,

.. code-block:: console

 $bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)

OR (If we dont have git installed )

.. code-block:: console

 Fetch installer script and run it ourself.
 $ curl -s https://rvm.beginrescueend.com/install/rvm -o rvm-installer

 $chmod +x rvm-installer
 $./rvm-installer --version latest

After installation you can see that a folder (`.rvm`) were created
in your home directory. This folder holds all RVM related files. Then to
activate `rvm` command for this user you have do one more step.

Add following line to your `.bashrc` file, so new shell session
onwards the `rvm` commands were available to this user. OR you can
just run bellow code in your current shell to activate it for this user
session only.


.. code-block:: console

 [[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" #
    This loads RVM into a shell session

Open a new shell session,
 
.. code-block:: console

 $ ruby --version
 ruby 1.8.7 (2010-08-16 patchlevel 302) [i486-linux]

 Current system ruby version
 $ rvm install 1.9.2

 This will install new ruby-1.9.2
 $ rvm install 1.9.1

 This will install new ruby-1.9.1
 $ rvm list
 rvm rubies
 ruby-1.9.1-p431 [ i386 ]
 ruby-1.9.2-p290 [ i386 ]

Now you can see that we have three versions of ruby in our system,
ruby-1.9.1 and ruby-1.9.2 were installed via RVM and ruby-1.8.7 from our
system. To switch between these versions,

To use ruby-1.9.1 in one shell session only, try bellow commands.

.. code-block:: console

 $rvm use 1.9.1
 $ruby --version
 ruby 1.9.1p431 (2011-02-18 revision 30908) [i686-linux]
 [/shell]
 To make this version change permanent for all user shell sessions use,
 [shell]
 $rvm --default use 1.9.1
 $rvm default list
 rvm rubies
 => ruby-1.9.1-p431 [ i386 ]
 ruby-1.9.2-p290 [ i386 ]

 This change will available to current and all new current user
    sessions.
 To get back to system ruby version
 $rvm reset

 $ruby --version
 ruby 1.8.7 (2010-08-16 patchlevel 302) [i486-linux]

Using RVM we can now set your suitable version of ruby, after that you
can install ruby gem packages using `gem` command of current ruby
version.

.. code-block:: console

 $ ruby --version
 ruby 1.8.7 (2010-08-16 patchlevel 302) [i486-linux]
 $ gem --version
 1.3.7
 $ rvm --default use 1.9.2
 Using /home/haridas/.rvm/gems/ruby-1.9.2-p290
 $ gem --version
 1.8.6

Check the gem versions while we switching between different version of
ruby.

Ok, thats it. Try out these tools.... have a happy hacking....:)

