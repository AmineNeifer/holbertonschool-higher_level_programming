#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_values(self):
        self.assertIsNone([])
        self.assertEqual([1, 2, 3, 4], 4)
        self.assertEqual([4, 2, 1, 3], 4)

