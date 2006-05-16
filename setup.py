#!/usr/bin/env python

import os
from distutils.core import setup, Extension

setup(
	name = 'pyanidb',
	version = 'svn',
	author = 'Vegard Eriksen',
	author_email = 'zyp@jvnv.net',
	url = 'http://dev.jvnv.net/misc/',
	packages = ['pyanidb'],
	scripts = ['anidb.py'])
