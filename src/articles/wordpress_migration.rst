Wordpress blog migrated to Pelican
==================================
:tags: wordpress,pelican,python
:category: blog
:date: 2012-05-07 13:33

Initially this blog was a wordpress blog. As you know the reasons for
that. Wordpress is the most successful and feature rich blogging engine. So
I chose it without any doubt. I didn't even search for a python alternative blog
engine at that time. But after a while I felt the dificulties while adding some
changes to the wordpress code, bugs with the wordpress plugins and more
importantly the Web UI is very annoying while typing new contents.


If we are considering the technical points, wordpress is a dynamic blog engine,
it is an over killing for blogs and other wiki based sites. Main issue is with speed of 
page rendering.The static pages are way faster compared to the dynamic contents. I know
wordpress has caching plugins to make the static pages out of dynamic one but
that are not a very reliable solution.

Actually above points are all come to my mind after seeing the static site
generators and their awesome features and flexibility. 

Advantages of static site generators over Dynamic blog engines
--------------------------------------------------------------

1. Serve html directly, so very fast.

2. Easy maintenance of the site, very less pain with server setup.

3. Use your favourite Text editors for blog posting. I use VIM :).

4. It use Markdown and Restructured Text Syntaxes for blog entry. So we just need to type 
   the post in normal text with simple formating. So don't worry about the
   html formatting while typing the content.

5. Host it on Github,  and very easy version control and site backup.

6. Very easy to customize the Themes  or other internals if you want.


Next step was which static site generator I will choose for my site. There are
a lot of them were implemented in Python and Ruby. I went through some of them
and finally chose `Pelican`_ a Python based static site generator.


`Jekyll`_
---------

Jekyll is a Ruby based system developed at github.com and it is very commonly
used in the Ruby world. I tried to use it because of its native github
support, but finally realized that we can do the same thing with other site
generators. And other problems I found with Jekyll was, 

- Its structure is difficult  compared to other site generators.
- It's a Ruby based one, I'm more comfortable with Python.


`Hyde`_
-------

Hyde is a  Python based static site generator like Jekyll and it removes some
of the difficulties with Jekyll. But it lacks good documentation, and mainly
a way to migrate from other blog engines like wordpress. I can see
that the project is evolving lately and got github site for documentation. But
it only covers the basics right now. I hope it will get good documentation very
soon.

`Pelican`_
----------

When I was very confused with different choices of static site generators, I came across 
Pelican (Another Python based static site generator.). It attracted me quickly
because of its,

* Simplicity
* Good Documentation
* Flexibility 
* Very easy way to use the Markdown texts. 

The documentation has everything required to migrate your blog from other blog
engines.And I liked the way it structured the blog posts and its contents.It
got clear upper hand over other site generators, I don't need to think twice to
select it.

Currently I hosted this site under Github, you can `fork`_ the project and give
a fresh try to see how quickly you can setup a blog.


.. _Pelican: http://pelican.notmyidea.org/
.. _Hyde: http://hyde.github.com
.. _Jekyll: http://jekyllrb.com/
.. _fork: https://github.com/haridas/haridas.github.com

