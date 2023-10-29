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

    def test_max_end(self):
        self.assertIs(max_integer([1, 3, 4, 5]), 5)

    def test_max_beginning(self):
        self.assertIs(max_integer([10, 3, 4, 5]), 10)

    def test_one_negative_num(self):
        self.assertIs(max_integer([-10, 3, 4, 5]), 5)

    def test_negative_nums(self):
        self.assertIs(max_integer([-10, -3, -4, -5]), -3)

    def test_one_element(self):
        self.assertIs(max_integer([-10]), -10)
