#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'flopska'
TAGLINE = 'Software dev and data science. Currently pursuing my PhD at KIT. In my free time I like to climb.'
SITENAME = 'flopska.com'
SITEURL = 'http://localhost:8000'
USER_LOGO_URL = '/images/logo.jpg'
ROUND_USER_LOGO = True
HIDE_USER_LOGO = False
THEME = '../pelican-svbhack'
LOAD_CONTENT_CACHE = False
PLUGINS = ['pelican_katex']

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', '/'),
    ('Publications', '/pages/publications.html'),
#    ('Books', '/category/books.html'),
#    ('Climbing', '/category/climbing.html'),
#    ('DIY', '/category/diy.html'),
    ('About', '/pages/about.html'),
)

PATH = 'content/pages'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('routestack', 'https://routestack.de/'),)

# Social widget
#SOCIAL = (('XING', 'https://www.xing.com/profile/Florian_Kalinke/cv'),
#        ('github.com/flopska','https://github.com/flopska'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
