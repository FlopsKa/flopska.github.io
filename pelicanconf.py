AUTHOR = 'Florian Kalinke'
SITENAME = 'flopska.com'
SITEURL = ''
USER_LOGO_URL = '/images/logo.jpg'
ROUND_USER_LOGO = True
HIDE_USER_LOGO = False
TAGLINE = 'Statistical machine learning.</br>Kernel methods.</br>Researcher at KIT.</br>Bouldering.'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_CATEGORIES_ON_MENU = False
PLUGINS = ['pelican_katex']

STATIC_PATHS = ["images", "publications", "CNAME"]

MENUITEMS = (
    ('Articles', '/articles.html'),
    ('Imprint / Impressum', '/legal-details.html'),

#    ('Books', '/category/books.html'),
#    ('Climbing', '/category/climbing.html'),
#    ('DIY', '/category/diy.html'),
#    ('About', '/pages/about.html'),
)

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = '../svbhack2'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## Shared katex conf across all files
KATEX_PREAMBLE = r"""
\renewcommand{\R}{\mathbb R}
\newcommand{\E}{\mathbb E}
\newcommand{\Var}{\mathrm{Var}}
"""
