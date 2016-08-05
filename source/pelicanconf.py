#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Liyosi Collins'
SITENAME = u'CKL'
SITEURL = ''
DEFAULT_LANG = u'en'
TIMEZONE = 'Africa/Nairobi'
OUTPUT_PATH = 'output/'
LOAD_CONTENT_CACHE = False

PATH = 'content'
STATIC_PATHS = ['static', 'blog', 'pages']
DEFAULT_LANG = u'en'
RELATIVE_URLS = False

AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'

ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'categories/{slug}.html'
CATEGORY_SAVE_AS = 'categories/{slug}.html'

TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'


# # Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = [
    ('Home', '/'),
    ('Projects', '/pages/projects/'),
    ('Books', '/pages/books/'),
    ('About', '/pages/about/'),
]

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'General'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

SUMMARY_MAX_LENGTH = 100

OUTPUT_RETENTION = ['.git']

IGNORE_FILES = ['.git']
DEFAULT_METADATA = {
    'status': 'draft',
}

DEFAULT_PAGINATION = 5
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/collins-liyosi-84903943'),
    ('github', 'https://github.com/liyocee'),
    ('stack-overflow', 'https://stackoverflow.com/users/1823036/liyosi'),
    ('twitter', 'https://twitter.com/collins.liyosi'),
    ('envelope', 'mailto:collinskivale@gmail.com')
)
THEME = 'themes/ckl'

# Theme settings
# HEADER_COLOR = 'black'
# HEADER_COVER = 'static/images/blog/ckl/banner.jpg'
COLOR_SCHEME_CSS = 'darkly.css'  # can be github.css; tomorrow.css; tomorrow_night.csc; darkly.css; monokai
# overriding section of the theme styling
CSS_OVERRIDE = 'static/css/ckl.css'
SHOW_FULL_ARTICLE = False
SHOW_SITESUBTITLE_IN_HTML = True
EXTRA_TEMPLATES_PATHS = [PATH + '/includes']
# my template settings
CURRENT_YEAR = 2016
AUTHOR_IMAGE_PATH = 'static/images/profile.png'
AUTHOR_URL = '/pages/about/'
