# coding: utf-8
from setuptools import setup, find_packages


setup(
    name='autodoc-c',
    version='0.1.0-dev',
    url='https://github.com/DasIch/autodoc-c',
    author='Daniel Neuhäuser',
    author_email='ich@danielneuhaeuser.de',

    packages=find_packages(),
    install_requires=['Sphinx>=1.2.2']
)
