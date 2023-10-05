#!/usr/bin/python3
"""This module supplies one function, add_integer(a, b=98)"""


def add_integer(a, b=98):
    """Returns the sum of a and b"""
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
