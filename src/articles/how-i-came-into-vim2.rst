My Vim Story 2
==============
:category: blog
:date: 02-08-2012
:title: Vim as your IDE


To follow this article you required basic idea of how to use Vim and its command
based basic editing.


In the first article_ I was describing how I came in to Vim editor and its
fundamental difference with other type of editors.
So on this article I'm explaining how to setup Vim as a common IDE for 
different programming languages. I'm basically a Python
guy, so I'm concentrate on Python side. But most of them are applicable to
other programming langauages also. Vim has bunch of plugins and other supports
available for all programming langauges. So no warry regarding that.

.. _article: http://haridas.in/my-vim-story-1.html 

Lets start to change the Vim as a simple editor to an IDE with Vim special
capability.The default Vim installed on most of the Gnu/Linux destros are more than
enough to do our works. But if you wan't more eye catchy look and feel and some
handy tools to do your work more quickly you need to install some Vim plugins,
good looking font's, color thems etc.

The Gnu/Linux Console based Vim has some limitation to show good font's and
colours. So you have to using GTK version of the Vim(Gvim). Gvim gives you all
the super looking features to your Vim. Just take a look
at my konsole based Vim and Gvim screen shots.



Vim on KDE Konsole
--------------------
.. image:: /images/vim-console.jpg
        :alt: vim-on-console
        :height: 400px
        :width: 768px
        :align: left


Gvim
----
.. image:: /images/gvim.jpg
    :alt: Gvim image
    :height: 400px 
    :width: 768px
    :align: left


I configured my Vim with set of Vim plugins to make it more productive.Bellow
I'm explaining all of them, and how to use my github vim settings available to
all of you, so that finaly you will get all of theses extra addition to your
vim and some nice scripts to handle them together.

Plugins
-------

1. MinibuferExplorer_.
2. Command-t_.
3. Syntastic_.
4. Snipmate_.
5. Fugitive_.
6. NerdTree_.
7. Nerdcommenter_.
8. Rope_.
9. Tagbar_.
10. SimplePairs_.

Above listed plugins are the main components of common IDE's. 

.. _MinibuferExplorer:

1. MinibuferExplorer
--------------------

This is like Tabs in other IDE's. We can see the opened files in vim using this
pluging. By default, we have to use `:ls` to see opened bufferes. So this
pluging makes very convienient to see the opened files as tabs.

Vim has slightly concept regarding the Tabs, compared to other IDE's. Vim has
support for tabs by default. That tab is different from the one we are
considered with the normal IDE's. Actually the difference is the vim tabs are
a collection of open bufferes(or files.). So we can consider it as grouping of
tabs in other IDE context.

But most of the time we only required one vim tab and set of opened
buffers(fiels.). Minibuffer Explorar help you to see those opened buffers as
a virutal tabs. See the bellow screen. 

.. image:: /images/minibufexplorer.jpg
    :height: 356px
    :width: 90%

You can use `CTRL + h/j/k/l` or `CTRL + w` to navigate around the different split windows and
the mini bufer Explorer. Try out that right away.

.. _Command-t:

2. Command-t
------------

Very awesome plugin for vim. Which help us to search the files very quickly.
Actually to get better speed it was implemented in C. To install this plugin
you need one extra compailation of this plugin because of C code. Don't warry
I explained this in the last section.

.. image:: images/command-t.jpg
    :width: 100%

Once we enabled this plugin you can see the search list using your 
`<leader> + t`. I'm using my leader key as **,**, so for me it looks like `,t`
(comma + t). Normally the leader key is '\'. 

Actually the leader key providers a extension to use all the keys in the 
keyboard as your own shortcuts. This leader key is activated in the normal mode of the
vim. 

Command-t also list the all opened buffers by `,b`, and it also list the vim
jumplist


.. _Syntastic:

3. Syntastic
------------

Another very useful plugin for all types of programming languages. 
This plugin helps to keep the syntax of the program correct, 
like auto correct in other IDE's. This package is general one, 
and we can expand very easily. By default it support lot of programming 
languages. So this plugin is a must one for Vim.

For example, if your are editing an RST file (All my blog posts are in
reStructured Text format), if we maid some syntax errors and when we 
trying to save, the syntastic plugin show you the
location of the error and its reason very neatly. 

Take a look at the rst format of this blog post. I maid a syntax error 
with image tag, 

.. image:: /images/syntastic.jpg
    :width: 100%

Similary synstastic help you to follow a standard coding methods defined by the
programming comunities. for eg; Python code has PEP8 standard, so while
writing python code, if you are not following it, synstastic will show you the
problem. After a while you will learn the PEP8 without an extra work :).


.. _Snipmate:

4. Snipmate
-----------

A simple way to avoid typing some repetative sequence of words. For example, in
python, we initilize a class by passing `class` keyword, name, etc... Instead
of doing all those drama, we can just populate the default set of class
structure from snipmate, by typing **cls** <tab>. Try out.

The snimpate plugin provide lot of such shortcuts for different programming
languages. We can also define our own snippets. For web developers this is very
usefull to create <table>, <div> tag completion. etc.

.. code-block:: bash

    vim test.py
    
.. code-block:: python

    #!/bin/python

    cl

After tying `cl` press tab and see the magic of full class template expansion.
similarly you can define you can define your own snipmate. for eg;
`for` <tab> to expand the `for` statement completely for you language.

You can see all the snipmate files inside this plugin folder, like
python.snipmate, ruby.snipmate etc.. The syntax of defining new snipmate for
your language is pretty interesting.


.. _Fugitive:

5. Fugitive
-----------

This is for git repo management inside vim itself. It provide set of short
commands, that we can driectly typed in the vim command mode to see and do the
git related operations. We don't need to go outside the editiing environment to
manage those stuffs. 

Also it have very nice git diff view inside vim itself, good looking and nice
to use.



.. _NerdTree:

6. NerdTree
-----------

Tree like display of all the files under your project. Very easy way to
navigate through all our directry structure, like other IDE's.

.. image:: /images/nerdtree.jpg

.. _NerdCommenter:

7. NerdCommenter
----------------

To comment and de-comment set of lines, this pluging provides set of easy
shorcuts. Other wise we have to do it manually. for eg;

<leader>cc,

.. _Rope:

8. Rope
-------

Rope is specially for python project navigation. Most of the IDE's have this
support to see the defenition of a function or class by clicking on it(or
via shortcut key).

By default, if we open a python project it won't have support for this
feature. When we trying to use this feature first time, the Rope prompt use to
create a ropeproject under our directory. This is just a simple settings file
under our project folder to specify different settings and path information.

The Plugin help us to create it easily, after that we can use this plugin to
view definition of all function or classes come under the rope project path.

In my Vim I mapped the **<leader>j** to :RopeGotoDefinition. For eg.

.. code-block:: python
    
    import os
    import sys

Keep your cursor on top of the `os` and press the <leader>j or
:RopeGotoDefinition, Vim will open the os file from the system path and open it
for you in the current Vim session as another buffer. Similarly we can go to
definition of any python entity definied under the Rope path. 

This also required one to meet the modern IDE feature list. :)

.. _Tagbar:

9. Tagbar
---------
This pluging is similar to the NerdTree, but instead of listing project
diretory structure it list the objects and functions inside a file. Like Class
browser in other IDE's.

.. image:: /images/tagbar.jpg
    :width: 100%

.. _SimplePairs:

10. Simple Pairs.
-----------------

This is a simple pluging to auto complete single quote, double quote,
parantheses, etc..



Fecthing from my git repo
-------------------------

Now lets see how we can setup vim to attain all the above fetures we discussed.
These Vim pluins and all are there in my Vim github_ project.

.. _github: https://github.com/haridas/Dotfiles/tree/master/vim-files

My git has already every vim related files. Only thing required is just clone
it and use it and do some steps to go ahead with all the features that
I discussed above.

.. code-block:: console

    git clone git://github.com/haridas/Dotfiles.git

    cd Dotfiles


I kept all the required plugins in git submodules. So we can easily get the new
changes from the plugin projects. While cloning my repo won't retrieve the
submodules or external plugin git projects. But we have all the settings and
paths in my git projects, so we can easily fetch the current stable code from
all the external projects. To do that, type bellow command, 

.. code-block:: console

    git submodules update


Now you have all the files required to get start with vim, one more step left
is link the my git files to your vim settings files. To do that just soft link
the files to git repo files. Here is the steps.

.. code-block:: console

    $cd
    $ln -s <path-to>Dotfiles/vim-files/vim .vim
    $ln -s <path-to>Dotfiles/vim-files/vim/vimrc .vimrc

Thats it, now open your vim, you can see all the features described above are
available, except command-t. Because it required a compilation. It has C code
to improve the speed. The compilation step is very simple. Follow me,

.. code-block:: console

    $ cd <path-to>Dotfiles/vim-files/vim/bundle/command-t/ruby/command-t
    $ ruby extconf.rb
    $ make

The make will succeed only when you have gcc and ruby support with vim. To check
the does ruby support avilable with your vim, open your vim and type,

.. code-block:: console
    
    :ruby 1

If there is no error, then you have ruby support with your vim. The latest
versions of vim has support with major dynamic languages like Python, Ruby and
others. So that won't give you any head ache.



SOME Vim short cuts
-------------------

.. code-block:: text

    In normal mode 
    ==============


    :23,30m200  -- move section of code to another line.

    df, (reverse dF,)     -- delete all characters till , one the current line.

    I  -- go your cursor to begining of the line as insert mode.

    $       -- in command mode, go to 

    gg  -- go to begining of the file

    G  -- go to end of the file.
    
    CTRL-O CTRL-I -- Jump list back and forward, very useful.

    CTRL + h/j/k/l -- move the control to different split windows.

    CTRL + F -- page down scroll.

    CTRL + B -- page back scroll.


