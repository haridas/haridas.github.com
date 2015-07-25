# -*- coding: utf-8 -*- #
import os

AUTHOR = u"HN"
SITENAME = u"HN"
# Don't, change the current URL scheme.
SITEURL = os.path.dirname(__file__)
#SITEURL = 'http://haridas.in'

TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

# Pagination settings.
DEFAULT_PAGINATION = 4
DEFAULT_ORPHANS = 2

# Theme settings.
THEME = os.path.join(os.path.dirname(__file__), 'src/templates/hn-theme')
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'pure.css'

# Ordering of content.
REVERSE_ARCHIVE_ORDER = True

# Other menu items
MENUITEMS = [('Archives', 'archives.html'),
             ('About', 'pages/about-me.html')]

# COVER_IMG_URL = "./images/Photz057.jpg"
PROFILE_IMG_URL = "images/profile_pic.jpg"

# External services and Social medias.

DISQUS_SITENAME = 'haridas'
GITHUB_URL = 'http://github.com/haridas'
GOOGLE_ANALYTICS = 'UA-23592173-1'
TWITTER_USERNAME = 'haridas_n'

# Blogroll
LINKS = (
)

# Social widget
#
# Make sure that the name of the images won't trigger addblock ;)
#
# Provide OPTIONAL (wxh) tuple if you want to resize the logo.
#
# FORMAT :- ( Label, logo, link, (width, height))
SOCIAL = (
    ('Twitter', 'images/tt.svg', 'http://twitter.com/haridas_n', ('48', '48')),
    ('Github', 'images/github.svg', 'http://github.com/haridas', ('45', '45')),
    ('Linkedin', 'images/linkedin.svg',
     'http://in.linkedin.com/pub/haridas-n/19/95/825', ('48', '48'))
)

ARTICLE_EXCLUDES = ['templates', 'pages', 'draft-articles']
PAGE_EXCLUDES = ['articles', 'drafts']
