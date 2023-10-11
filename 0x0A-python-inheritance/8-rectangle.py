#!/usr/bin/python3
""" this module consists only of two classes: BaseGeometry
    and its subclass Rectangle"""


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


class Rectangle(BaseGeometry):
    """a subclass of the base class BaseGeometry
        that represents a rectangle"""
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.height = super().integer_validator("height", height)
