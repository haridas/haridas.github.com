# -*- coding: utf-8 -*- #

AUTHOR = u"Haridas N"
SITENAME = u"Haridas N"
# Don't, change the current URL scheme.
SITEURL = '.'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

# Pagination settings.
DEFAULT_PAGINATION = 4
DEFAULT_ORPHANS = 2

# Theme settings.
THEME = '/mnt/data/projects/github/haridas.github.com/src/templates/pure-single'
THEME_STATIC_PATHS = ['static']
#CSS_FILE = 'main.css'
CSS_FILE = 'pure.css'

# Ordering of content.
REVERSE_ARCHIVE_ORDER = True

# Other menu items
MENUITEMS = [('Archives', '/archives.html'),
             ('About', '/pages/about-me.html')]

COVER_IMG_URL = "images/Photz057.jpg"
PROFILE_IMG_URL = "images/Image022.jpg"

## External services and Social medias.

DISQUS_SITENAME = 'haridas'
GITHUB_URL = 'http://github.com/haridas'
GOOGLE_ANALYTICS = 'UA-23592173-1'
TWITTER_USERNAME = 'haridas_n'

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
    ('twitter-square', 'http://twitter.com/haridas_n'),
    ('github', 'http://github.com/haridas'),
    ('linkedin', 'http://in.linkedin.com/pub/haridas-n/19/95/825'),
)

ARTICLE_EXCLUDES = ['templates', 'pages']
PAGE_EXCLUDES = ['articles', 'drafts']
