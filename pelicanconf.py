#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ronny Pfannschmidt'
SITENAME = u'Blargh'
SITEURL = ''

PATH = 'content'
THEME = 'chunk'
TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}.html'
ARTICLE_URL = 'posts/{date:%Y}/{slug}.html'

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
