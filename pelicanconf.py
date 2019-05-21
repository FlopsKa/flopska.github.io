#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'flopska'
TAGLINE = 'Software dev and data science. Currently pursuing my M.Sc. in Computer Science at KIT. In my free time I like to climb.'
SITENAME = 'flopska.com'
SITEURL = 'http://localhost:8000'
USER_LOGO_URL = SITEURL + '/images/logo.jpg'
ROUND_USER_LOGO = True
HIDE_USER_LOGO = True
THEME = 'pelican-svbhack'
LOAD_CONTENT_CACHE = False

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
#MENUITEMS = (
#    ('Home', '/'),
#    ('CS', '/category/cs.html'),
#    ('Books', '/category/books.html'),
#    ('Climbing', '/category/climbing.html'),
#    ('DIY', '/category/diy.html'),
#    ('About', '/pages/about.html'),
#)

PATH = 'content'

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