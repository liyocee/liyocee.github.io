#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://liyosi.me'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Following items are often useful when publishing

DISQUS_SITENAME = 'liyosi'
GOOGLE_ANALYTICS = 'UA-67190565-3'
ADDTHIS_PUBID = 'ra-57adf2ff04087e24'
