# -*- coding: utf-8 -*-
"""Packaging logic for Flake8-JSON."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))  # noqa

import flake8_for_pycharm
import setuptools

setuptools.setup(
    version=flake8_for_pycharm.__version__,
    # NOTE(sigmavirus24): Remove this and uncomment the lines in setup.cfg
    # after https://github.com/pypa/setuptools/issues/1136 is fixed
    package_dir={
        '': 'src/',
    },
    scripts=('bin/flake8_pycharm.py',)
)
