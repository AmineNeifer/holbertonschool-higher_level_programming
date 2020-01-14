#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_values(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)
        self.assertEqual(max_integer([1, 4, 2, 1]), 4)
        self.assertEqual(max_integer([-1, 2, 6, 5]), 6)
        self.assertEqual(max_integer([1, 5, 5, 1]), 5)
        self.assertEqual(max_integer([1]), 1)
        with self.assertRaises(TypeError):
            max_integer([])
            max_integer(["3", 2])
            max_integer([2, 3, 4, 7, "amine"])
