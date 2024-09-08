# -*- coding: utf-8 -*-
"""
Base test case
"""
import logging
from os import path
from unittest import TestCase

logging.basicConfig(level=logging.CRITICAL)

LOGGER = logging.getLogger(__name__)

SOURCE_DIR = path.dirname(path.dirname(__file__))

PKGNAME = "adsp"


class BaseTestCase(TestCase):
    """
    Test any class
    """

    @classmethod
    def setUpClass(cls):
        cls.longMessage = True
        cls.maxDiff = None
