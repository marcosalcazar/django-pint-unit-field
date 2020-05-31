#!/usr/bin/env python

from setuptools import setup, find_packages
import os

__version__ = '0.1.0'

PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))
os.chdir(PACKAGE_DIR)


setup(name='django-pint-unit-field',
      version=__version__,
      url='https://github.com/marcosalcazar/django-pint-unit-field',
      author="Marcos Gabriel Alcázar",
      author_email="marcos.alcazar@gmail.com",
      description=("Unit Field for Django using pint library "
                   "for automated unit conversions"),
      long_description=open(os.path.join(PACKAGE_DIR, 'README.md')).read(),
      license='MIT',
      packages=find_packages(exclude=["tests*"]),
      include_package_data=True,
      install_requires=[
          'django>=3.0',
          'pint>=0.12',
          ],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python']
      )
