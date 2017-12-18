Vim Upgrade 2017
================

:date: 2017-12-18
:tags: vim
:slug: vim-upgrade-2017
:summary: Vim upgrade with new set of plugins.
:category: blog

After using vim for few years the main difficulties I have with my current
pathogen based vim plugin environment is, it's bit difficult to re-produce a
fresh setup on new machine, managing gitmodules is dirty thing and adding new
plugins and playing around with it is not straight. So I realized new plugins and
plugin managers available now are well fit to address these problems. So here
I'm logging the cosmetic and plugin changes done on my latest vim environment.

Setup Vim configurations
------------------------

.. image:: /images/setup-vim.gif
        :alt: vim-setup
        :align: left
        :width: 100%
        :height: 400px

The commands shown in this gif are given bellow.

For all plugins go to https://vimawesome.com site.

vim-plug
---------

Now switched to new plugin manager `vim-plug`. This is very minimalistic and
easy to use compared to pathogen. Also don't need to manage the plugins via git
submodules. Reproducing the setup on a new system is much simpler now.  With this 
plugin manager you can easily try out new plugins, lazy load the plugins when
need it etc.

Plugin list
-----------

    1. fzf.vim_.
    2. ack.vim_.
    3. Syntastic_.
    4. NerdTree_.
    5. LanguageSpecific_.
    6. VimThemeRelated_.

.. _fzf.vim:

1. FZF
-------

Fuzzy file search and buffer search, better than `Command-t` and there is no 
separate manual step needed to set it up when using with `vim-plug`. This plugin
also relay on `.gitignore` file to filter out the unnecessary files from search.

Dependency: golang1.9.x+ installed in your box.

.. _ack.vim:

2. Silver searcher
------------------

If you not yet have it, then this one is must needed plugin for vim. This plugin
depends on the command `ag (silver searcher)` on your machine, if it's not installed, install it
from package manager.

Grep a keyword across the source directory, this is common feature in full fledged 
IDE's. Here we use the silver search with the ack.vim plugin to get the ag
capabilities inside vim, also easy navigation on search results.

.. _NerdTree:

3. NerdTree
------------

Standard plugin to list the project directories.

.. _Syntastic:

3. Code syntax check using lint tools.
--------------------------------------

1. Syntastic: Pretty standard generic syntax issue identifier and reporter.

.. _LanguageSpecific:

4. Language plugins
-------------------
These plugins we can load when we open those language files only, vim-plug have
option to do this when configure the plugin with it. See bellow section for the sample
vim-plug configuration.

1. vim.go : Make vim more friendly in vim, do re-format, highlight issues etc.
2. rust.vim.git
3. vim-ansible-yaml.git


.. _VimThemeRelated:

5. Vim Theme Related.
---------------------

1. vim-color-solaraized

   Nice vim color plugin for all environments and language, i would recommend it
   for all.

2. vim-airline
   This will add some nice colors to your bottom vim status bar and shows good
   information about the editing status and all.


Example vimrc snippat for plugin.

.. code-block:: vim

    Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }
    Plug 'https://github.com/scrooloose/syntastic.git'
    Plug 'https://github.com/fatih/vim-go.git', { 'for': 'go'}
    Plug 'https://github.com/chase/vim-ansible-yaml.git'
    Plug 'https://github.com/mileszs/ack.vim.git'
    Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
    Plug 'junegunn/fzf.vim'
    Plug 'altercation/vim-colors-solarized'


How to setup this Environment.
------------------------------

.. code-block:: bash

    git clone https://github.com/haridas/Dotfiles.git ~/Dotfiles
    ln -s ~/Dotfiles/vim-files/vim ~/.vim
    ln -s ~/Dotfiles/vim-files/vimrc ~/.vimrc

Now ready to install all plugins with single command `:PlugInstall`. See bellow
highlight.


Possible errors
---------------

1. Sigfault when running :PlugInstall command

This is mainly comes when the ruby binding compiled with vim might have some issue,
try this `:ruby print "hello"`, this might reproduce the segfault issue. In this case
get a fresh vim version or ensure vim got latest ruby bindings.

References
----------

1. https://vimawesome.com
