#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    class for testing Base class
    """
    def test_max_integer(self):
        """Auto assign ID exists"""
        b1 = Base()
        self.assertEqual(b1.id, 1)