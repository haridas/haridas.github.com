My Vim Story 2
==============

How to setup VIM as an IDE.
---------------------------

In the last article I described what thing made me to use VIM as my main
Editor. So on this article I'm trying to explaing how to setup Vim with
required plugins for different programming languages. I'm basically a Python
guy, so I'm concentrate on Python side. But most of them are applicable to
other programming langauages. You can find out more some of specific plugins
that helps to do more effective work with your favorite programming language.

The default Vim installed with most of the Gnu/Linux destros are more than
enough to do our work. But if you wan't more eye catch look and feel and some
handy tools to do your work more quickly you need to install some Vim plugins,
font's, color thems etc.

The Gnu/Linux Console based Vim has some limitation to show good font's and
colours. So you have to using GTK version of them Vim. Gvim. Gvim give you all
the super looking features to your vim with all Vim features. Just take a look
at my Console based Vim and Gvim screen shots.

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

So the things we need to modify with the default Vim to get the above look and
feel, you have to change and update following things,

1. Fonts and Syntax Coloring theme.
2. Setup plugin environment.
3. Add required plugins.


I configured my Vim with following Plugins

Plugins
-------

1. MinbufferExplorar
2. Command-t
3. NerdTree.
4. Nerdcommenter
5. Rope
6. Simple commenter
7. Snipmate
8. Syntastic
9. Tagbar
10. Fugitive

Above listed plugins are the most usable for Python projects. In which most of
them are general purpose one, so it will suitable for other programming
languages also.

1. minibufferExplorar
---------------------

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

Thats it now open your vim, you can see all the features described above are
available, except command-t. Because it required a compilation. It has C code
to improve the speed. The compilation step is very simple. Follow me,

.. code-block:: console

    $ cd <path-to>Dotfiles/vim-files/vim/bundle/command-t/ruby/command-t
    $ ruby extconf.rb
    $ make

The make will succeed only when you have gcc and ruby support to vim. To check
the does ruby support avilable with your vim, open your vim and type,

.. code-block:: console
    
    :ruby 1

If there is no error, then you have ruby support with your vim. The lates
versions of vim has support with major dynamic languages like Python, Ruby and
others. So that won't give you any head ache.
