#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"haridas"
SITENAME = u"haridas.in"
SITEURL = '/'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG='en'

# Pagination settings.
DEFAULT_PAGINATION = 4
DEFAULT_ORPHANS = 2

# Theme settings.
THEME = '/usr/local/lib/python2.7/dist-packages/pelican/themes/notmyidea'
THEME_STATIC_PATHS = ['static']
#CSS_FILE = 'main.css'


## External services and Social medias.

DISQUS_SITENAME = 'haridas'
GITHUB_URL = 'http://github.com/haridas'
GOOGLE_ANALYTICS = ''
TWITTER_USERNAME = 'haridas_n'

# Blogroll
LINKS =  (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
         )

# Social widget
SOCIAL = (
        ('twitter', 'http://twitter.com/haridas_n'),
        ('github','http://github.com/haridas'),
        ('linkedin', 'http://in.linkedin.com/pub/haridas-n/19/95/825'),
         )

PAGE_EXCLUDES = ['articles','drafts',]


    
