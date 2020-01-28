#!/usr/bin/python3
""" Unittest testing for Base class instances"""


import unittest
from models.base import Base


class testBase(unittest.TestCase):
    """ test Base methods"""

    def test_init(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
