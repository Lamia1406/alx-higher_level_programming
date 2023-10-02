#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains a class named Rectangle """


class Rectangle:
    """This class is empty"""
    def __init__(self, width=0, height=0):
        """Initialize a new instance of the Rectangle
        Args:
            width:  defining the width of the rectangle
            height: defining the height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to set the width
        Args:
            value: the width of the rectangle to set:
                - must be an integer
                - must be >= 0
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to set the height
        Args:
            value: the height of the rectangle to set:
                - must be an integer
                - must be >= 0
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
