#!/usr/bin/python3
"""This module contains only one class : class Square(Rectangle)"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """subclass of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of the size of a square(width and height are equal)"""
        return self.width

    @size.setter
    def size(self, size):
        """setter of the size of a square (width and height are equal)"""
        self.width = size
        self.height = size

    def __str__(self):
        """return the string representation of the square"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
