#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'Markdown',
    version = '2.0-beta-2',
    description = "Python implementation of Markdown.",
    author = "Manfred Stienstra and Yuri takhteyev",
    author_email = "yuri [at] freewisdom.org",
    maintainer = "Waylan Limberg",
    maintainer_email = "waylan [at] gmail.com",
    url = "http://www.freewisdom.org/projects/python-markdown",
    license = "BSD License",
    packages = ['markdown', 'markdown.extensions'],
    scripts = ['markdown.py'],
    ) 
