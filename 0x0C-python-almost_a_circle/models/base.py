#!/usr/bin/python3
"""This module contains only one class : class Base"""


class Base:
    """creates objects with an optional unique ID
    - maintain a count of how many objects have been created from it.
    - if no ID is specified, it assigns the current count as the ID
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
