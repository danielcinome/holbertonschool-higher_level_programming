#!/usr/bin/python3
"""
Module for unittests for the Base class
"""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import json

def test_pep8_conformance_base(self):
        """Test that we conform to PEP8."""
        pycodestyle = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

"""------- TASKS 1 ------"""
class TestBaseClassCreation(unittest.TestCase):
    """Test class for Base class instantiation tests"""

    def test_id_positive(self):
        bo = Base(23)
        self.assertEqual(bo.id, 23)
        bo = Base(34)
        self.assertEqual(bo.id, 34)

    def test_id_negative(self):
        bo = Base(-4)
        self.assertEqual(bo.id, -4)
        bo = Base(-10)
        self.assertEqual(bo.id, -10)

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, 1)
        bo = Base(None)
        self.assertEqual(bo.id, 2)

    """------- TASKS 15 ------"""
    def test_dictionary(self):
        """comment"""
        rel = Rectangle(10, 7, 2, 8, 70)
        dictionary = rel.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_dictionary_empty(self):
        """Comment"""
        dictionary = []
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, "[]")

        obj = None
        json_dictionary = Base.to_json_string(obj)
        self.assertEqual(json_dictionary, "[]")
