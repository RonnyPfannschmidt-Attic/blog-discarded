#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ronny Pfannschmidt'
SITENAME = 'all the things'
SITEURL = ''
SINGLE_AUTHOR = True
PATH = 'content'
THEME = 'chunk'
TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'
ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Blogroll
LINKS = (
    #('Pelican', 'http://getpelican.com/'),
)
# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/ossronny'),
    ('Google+', 'https://plus.google.com/+RonnyPfannschmidt/posts'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
