#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains a class named Square """


class Square:
    """ this class defines a square
    Args:
        size: Private instance attribute defining the size of a square
                that is of int type and absolutely positive
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """The area method returns the current square area """
        return self.__size ** 2

    @property
    def size(self):
        """ size getter : to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter : to set it
        Args:
            value : the size value (should be an int)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
