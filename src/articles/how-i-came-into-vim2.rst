My Vim Story 2
==============
:category: blog
:date: 02-08-2012
:title: Vim as your IDE


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


.. _Command-t:

2. Command-t
------------

Very awesome plugin for vim. Which help us to search the files very quickly.
Actually to get better speed it was implemented in C.

Screen shot.

.. _Syntastic:

3. Syntastic
------------

Another very useful pluging for all types of programming. This pluging helps to
keep the syntax of the program correct, like auto correct in other programming
language. This package is general one, and we can expand very easily. By
default it support lot of programming languages. So this plugin is a must one
for Vim.

Screen shot.

.. _Snipmate:

4. Snipmate
-----------

Helps to write a our own code macros, and can be used with any programming
language. We can define a code block that need to prefilled when we type
a keyword and tab. For example, in python to do a pdb,

import pdb
pdb.set_trace() - required. 

To make a snipmate 

pdb<tab> -- expands to import pdb; pdb.set_trace()

Some samples.

.. _Fugitive:

5. Fugitive
-----------

This is for git repo management inside vim itself. It provide set of short
commands, that we can driectly typed in the vim command mode to see and do the
git related operations. We don't need to go outside the editiing environment to
manage those stuffs. 

Screen shots.

.. _NerdTree:

6. NerdTree
-----------

Tree like display of all the files under your project. Very easy way to
navigate through all our directry structure, like other IDE's.

Screen shot.

.. _NerdCommenter:

7. NerdCommenter
----------------

To comment and de-comment set of lines, this pluging provides set of easy
shorcuts. Other wise we have to do it manually. for eg;

<leader>cc,

.. _Rope:

8. Rope
-------
Rope is specially for python code jumping. For other programming languages have
their cross file code navigation using similar tools. for eg;

.. _Tagbar:

9. Tagbar
---------
This pluging is similar to the NerdTree, but instead of listing project
diretory structure it list the objects and functions inside a file. Like Class
browser in other IDE's.

Scree Shots.

.. _SimplePairs:

10. Simple Pairs.
-----------------

This is a simple pluging to auto complete single quote, double quote,
parantheses, etc..




Fecthing from my git repo
-------------------------

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
