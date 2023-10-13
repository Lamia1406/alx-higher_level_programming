#!/usr/bin/python3
""" this module consists only of one classe: Square
    that is the subclass of Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass of the class Rectangle
        that represents a square"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """return the string description of a square"""
        return f"[Square] {self.__size}/{self.__size}"
