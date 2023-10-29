#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertIs(max_integer(), None)

    def test_zero_len(self):
        self.assertIs(max_integer([]), None)

    def test_type_None(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_not_list(self):
        with self.assertRaises(TypeError):
            max_integer(123)

    def test_regular(self):
        self.assertIs(max_integer([1, 3, 4, 2]), 4)
