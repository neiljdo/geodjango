# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import geodjango
version = geodjango.__version__

setup(
    name='geodjango',
    version=version,
    author='',
    author_email='neiljohn.ortega@gmail.com',
    packages=[
        'geodjango',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['geodjango/manage.py'],
)