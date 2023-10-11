#!/usr/bin/python3
""" this module consists only of two classes: BaseGeometry
    and its subclass Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass of the base class BaseGeometry
        that represents a rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the string description o fa rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
