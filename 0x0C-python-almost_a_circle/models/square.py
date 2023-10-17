#!/usr/bin/python3
"""This module contains only one class : class Square(Rectangle)"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """subclass of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """return the string representation of the square"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")
