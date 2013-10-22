#!/usr/bin/env python
import os
from distutils.core import setup, Command


setup(
    name='wafti-news',
    version='0.0.0',
    packages=['news_rhino', 'wafti_news'],
    url='http://wafti.org.uk/news/',
    license='GPL v2',
    author='Ross Fenning',
    author_email='ross.fenning@wafti.org.uk',
    description='WAFTI News'
)

