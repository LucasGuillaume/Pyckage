#!/usr/bin/env python

from setuptools import setup, Extension, find_packages
import os
import sys

setup(
    name='[NAME]',
    version='[VERSION]',
    description="[DESCRIPTION]",
    long_description="[LONG DESCRIPTION]",
    author='[AUTHOR]',
    author_email="[AUTHOR_EMAIL]",
    packages=find_packages("."),
    url="[URL]",
    python_requires='[REQUIRES]',
    package_data={'[NAME]': ['resources/*']},
    entry_points={'console_scripts': [
        "[NAME] = [NAME].launchers.[NAME]_launcher:main",
    ]},
)
