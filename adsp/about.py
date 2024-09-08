# -*- coding: utf-8 -*-
"""
About this package
"""
from os.path import basename, dirname

from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

__description__ = (
    "Retrieve stop and search data from the Metropolitan Police Service API"
)
__author__ = "Tinashe Wamambo"
__author_email__ = "tinashe.wamambo@hotmail.co.uk"
__pkgname__ = basename(dirname(__file__))
