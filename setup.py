#!/usr/bin/env python

import os
import sys

from os.path import join, dirname, abspath
from setuptools import setup, find_packages

sys.path.insert(0, join(dirname(abspath(__file__)), 'contrib'))

def find_data_files(dirs):
    result = []
    for x in dirs:
        for dirpath, _, filenames in os.walk(x):
            result.append((
                dirpath,
                [os.path.join(dirpath, y) for y in filenames],
            ))
    return result

setup(
    name='musicdb',
    scripts=('musicdb/manage.py',),
    packages=find_packages(),
    zip_safe=False,
    data_files=find_data_files(('media', 'templates')),
    test_suite='setuptest.setuptest.SetupTestSuite',
)
