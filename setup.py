import os
import sys
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "weber", "__version__.py")) as version_file:
    exec(version_file.read()) # pylint: disable=W0122

_INSTALL_REQUIRES = [
    'Jinja2',
]

if sys.version_info < (3, 0):
    _INSTALL_REQUIRES.append('contextlib2')

setup(name="weber",
      classifiers = [
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: py",
          ],
      description="A tool for building and deploying robust web applications in Python",
      license="BSD3",
      author="Rotem Yaari",
      author_email="vmalloc@gmail.com",
      version=__version__, # pylint: disable=E0602
      packages=find_packages(exclude=["tests"]),

      url="https://github.com/vmalloc/weber",

      install_requires=_INSTALL_REQUIRES,
      scripts=[],
      namespace_packages=[]
      )
