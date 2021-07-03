#!/usr/bin/env python

from setuptools import setup, Extension, find_packages
import os
import sys

setup(
    name='pyckage',
    version='0.1',
    description="Create python packages easily (boilerplate)",
    long_description="No long description available",
    author='DELEVOYE Guillaume',
    author_email="delevoye.guillaume@gmail.com",
    packages=find_packages("."),
    url="https://github.com/LucasGuillaume/Pyckage",
    install_requires=['tqdm'],
    package_data={'pyckage': ['resources/*']},
    entry_points={'console_scripts': [
        "pyckage = pyckage.launchers.pyckage_launcher:main",
    ]},
)
