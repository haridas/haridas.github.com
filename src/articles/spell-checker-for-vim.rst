Spell Checker for Vim
#####################
:date: 2015-06-28
:category: programming
:tags: vim


As a long time vim user I always have troubles with typos in vim. Vim has inbuilt
spell checker tool, but it's little cumbersome to use. I use vim for
most of the purposes like,

1. To write my blog entries.
2. Coding
3. To write git commit messages, where I get some typos. This one is more annoying
   than typos in any other places.
4. Coding in any languages except Java ;).


So what usually happens was I miss some types on git commits or comments
that I put while coding. Before using this plugin I use the inbuilt vim spell
checker directly, to access that you have to type this command in the command mode,

.. code-block:: vimscript

    :setlocal spell spelllang=en_us

Most of the time I forgot this full command and I have to issue `:help spell` to
get this command :). What was other annoying problem is, after checking the spell
corrections, I need a quick way to disable the spell check highlights. With the
inbuild spell checker you need to type the following command to disable it.

Unset the spell variable to disable the highlights, 

.. code-block:: vimscript

    :setlocal spell spellang=

Eventually these typos are started to come and bite me. So I was started to look 
for an easy way to achieve spell check. I don't want to use any new plugin for this
feature. I want to use the inbuilt vim spell checker itself but in more saner way.
So to get that done I wrote simple function in vimscript and put it in the `~/.vimrc`.
Thats it.

So after putting this script, I only need to type `<leader>c` to enable the
spell check and `<leader>c` again to toggle the spell check.

Here is the function that you can put it in your vimrc file to get these spell 
check bindings



.. code-block:: vimscript

    " > Spell checker Toggler <

    nnoremap <leader>c :call SpellChecker()<cr>

    let g:spell_checker_is_active = 0
    function! SpellChecker()
        if g:spell_checker_is_active
            setlocal spell spelllang=
            let g:spell_checker_is_active = 0
        else
            setlocal spell spelllang=en_us
            let g:spell_checker_is_active = 1
        endif
    endfunction

    " > End of spell check toggler <

To see this in action see the bellow gif.

.. image:: images/spell-check.gif
    :height: 400px
    :width: 100%
    :align: left



If you are using my vim package from the github, then this feature is already
there. Or if you want only this feature just copy paste above vimscript function
in your vimrc file.


Reference
---------
1. `Learn Vim The Hardway`_

.. _`Learn Vim The Hardway`: https://learnvimscriptthehardway.stevelosh.com/
