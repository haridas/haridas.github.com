# -*- coding: utf-8 -*- #
import os

AUTHOR = u"HN"
SITENAME = u"HN"
# Don't, change the current URL scheme.
#SITEURL = 'http://localhost:8000'
#
SITEURL = 'https://haridas.in'

TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

# Pagination settings.
DEFAULT_PAGINATION = 4
DEFAULT_ORPHANS = 2

# Theme settings.
THEME = os.path.join(os.path.dirname(__file__), 'src/templates/hn-theme')
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'pure.css'

# Ipython template directory setting.
IPYTHON_TEMPLATE_PATH = os.path.join(os.path.dirname(__file__),
                                     "src/ipython_templates")

# Ordering of content.
REVERSE_ARCHIVE_ORDER = True
#
# Properly resolve the URLs for each articles. THere is no nesting all the
# blog entries are kept on the top level itself.
CATEGORY_SAVE_AS='category/{slug}.html'
CATEGORY_URL='category/{slug}.html'
TAG_URL='tag/{slug}.html'
TAG_SAVE_AS='tag/{slug}.html'
ARTICLE_URL='/{slug}.html'

# Other menu items
MENUITEMS = [
    #('Archives', 'archives.html'),
    ('Programming', 'category/programming.html'),
    ('Data-Science', 'category/data-science.html'),
    ('Security', 'tag/security.html'),
    ('Devops', 'category/devops.html'),
    ('Gists', 'https://gist.github.com/haridas'),
    ('About Me', 'pages/about-me.html'),
    ('Resume', 'resume.pdf')
]

# COVER_IMG_URL = "./images/Photz057.jpg"
PROFILE_IMG_URL = "images/profile_pic.jpg"

# External services and Social medias.

DISQUS_SITENAME = 'haridas'
GITHUB_URL = 'http://github.com/haridas'
GOOGLE_ANALYTICS = 'UA-23592173-1'
TWITTER_USERNAME = 'haridas_n'

MARKUP = ('md', 'ipynb', 'rst', 'adoc')
# Ascii doc markup settings.
ASCIIDOC_CMD = 'asciidoctor'
ASCIIDOC_OPTIONS = []
ASCIIDOC_BACKEND = 'html5'
PLUGIN_PATHS = (os.path.join(os.path.dirname(__file__), './pelican-plugins'),)
# plugins.
PLUGINS = [
    "pelican_gist",
    "pelican-ipynb.markup",
    "asciidoc_reader.asciidoc_reader",
    "render_math"
]

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
     'https://linkedin.com/in/haridasn', ('48', '48'))
)

ARTICLE_EXCLUDES = ['templates', 'pages', 'draft-articles']
PAGE_EXCLUDES = ['articles', 'drafts']
