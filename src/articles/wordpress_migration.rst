Wordpress blog migrated to Pelican
==================================
:tags: wordpress,pelican,python
:category: programming
:date: 2012-05-07 13:33


Initially this blog was running on wordpress, And you know the reasons for
that. Wordpress is the most successful and feature rich blog engine. So
I chose it without thinking twice, I didn't even search for a python alternative blog
engines at that time. But after a while I felt the difficulties while adding some
changes to the wordpress code, bugs with the wordpress plugins and more
importantly the Web based editor is very annoying while typing new contents.


If we are considering the technical points, wordpress is a dynamic blog engine,
it is an overkill for simple blogs and other wiki based sites. Main issue is the speed of 
page rendering.The static pages are way faster than the dynamic pages. I know
wordpress has caching feature to improve the speed of the page rendering,but it
is not a simple solution.

Actually above points are all came to my mind after seeing the static site
generators and their awesome features.

Advantage of static site generators over Dynamic blog engines
--------------------------------------------------------------

1. Serve html files directly, so very fast.

2. Easy maintenance of the site, very less pain with server setup.

3. Use your favourite text editor for blog posting. I'm a VIM fan :).

4. It uses Markdown or Restructured Text Syntax for blog entry. So we just need to type 
   the post in normal text with simple formating. So we don't need to worry about the
   html formatting while typing the content.This feature were attracted me more
   because the wordpress web editor sucks, and here I can use Vim.

5. Host it on Github,Bitbucket. The entire blog is a set of text files that 
   enables easy version controlling.

6. Very easy to customize the Themes  or other internal structure. 


Next challenge that I faced was the selection of one static site generator from 
bunch of choice. There are lot of them are implemented in
Python or Ruby. I was searched for few days to come up with a suitable one.
Finally I picked up a Python based engine `Pelican`_ as my favorite. It doesn't
mean that others are bad implementation, but Pelican suits my taste better.

Here is the list of few major static site generators that I went through as
part of the selection process.

`Jekyll`_
---------

Jekyll is a Ruby based system developed at github.com and it is very commonly
used in Ruby world. I tried to use it because of its native github
support, but finally I realized that we can do the same thing with other site
generators, And other problems that I found on Jekyll was, 

- Its structure is difficult compared to other site generators.
- It's a Ruby based one, I'm more comfortable with Python.


`Hyde`_
-------

Hyde is a  Python based static site generator like Jekyll but less complex.
But Hyde lacks good documentation, and mainly a way to migrate from other 
blog engines. I can see that the project getting more interest recently.
I hope it will get in to good position very soon.

`Pelican`_
----------

After checking different static site generators I was very confused with 
different types of static site generators that I came across. Finally I got the
one I'm looking for, Pelican (Another Python based static site generator.). The
reason for picking Pelican was very simple.

* Simplicity
* Good Documentation
* Flexibility 
* Very easy way to use the Markdown texts. 

The documentation has everything required to migrate your blog from other blog
engines.And I liked the way it structured the blog posts and its contents.It
got clear upper hand over other site generators, I don't need to think twice to
select it.

Currently I hosted this site under Github, you can `fork`_ this project and give
a fresh try to see how quickly you can setup a blog.


.. _Pelican: https://pelican.notmyidea.org/
.. _Hyde: https://hyde.github.com
.. _Jekyll: https://jekyllrb.com/
.. _fork: https://github.com/haridas/haridas.github.com

