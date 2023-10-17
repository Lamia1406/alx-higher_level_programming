#!/usr/bin/python3
"""This module contains only one class : class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """subclass of Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    @property
    def width(self):
        """getter of the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter of the width of a rectangle"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter of the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter of the height of a rectangle"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter of the x coordinate the rectangle should be displayed"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter of the x coordinate the rectangle should be displayed"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter of the y coordinate the rectangle should be displayed"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter of the y coordinate the rectangle should be displayed"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle with character #"""
        for space in range(self.__y):
            print()
        for ligne in range(self.__height):
            print((self.x * " ") + ("#" * self.width))

    def __str__(self):
        """return the string representation of the rectangle"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
