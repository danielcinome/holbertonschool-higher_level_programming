#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(max_integer([1, 2, 7, 4]), 7)
        self.assertEqual(max_integer([[1230], [2321], [6534], [5432]]), [6534])
        self.assertEqual(max_integer([-988, 765]), 765)
        self.assertEqual(max_integer([3]), 3)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            max_integer([2, 3, "Holberton"])
        with self.assertRaises(TypeError):
            max_integer(4, 5)

    def test_Empty_list(self):
        self.assertIsNone(max_integer())
