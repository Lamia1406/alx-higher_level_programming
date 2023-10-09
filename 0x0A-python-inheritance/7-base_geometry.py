#!/usr/bin/python3
""" this module consists only of one class: BaseGeometry"""


class BaseGeometry:
    """an class with two instance methods"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value: it must be >=0 int """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
