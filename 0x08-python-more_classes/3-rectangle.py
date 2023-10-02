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
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
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

    def area(self):
        """ Computes the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Computes the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Prints the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        for i in range(self.__height):
            string += ("#" * self.__width)
            if i < self.__height - 1:
                string += "\n"
        return string
