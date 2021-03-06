#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nick Cook'
SITENAME = 'Minimum Viable Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = '/mnt/c/Programming/Pelican/mvb/pelican-themes/pelican-clean-blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/nick-cook-b3749a7a/'),
          ('github', 'https://github.com/nickcook530'),)

DEFAULT_PAGINATION = False

#Clean-blog configuration
HEADER_COLOR = 'darkcyan'
#COLOR_SCHEME_CSS = 'tomorrow_night.css'
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True