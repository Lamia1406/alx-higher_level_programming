#!/usr/bin/python3
"""This module contains only one class : class Base"""
import json


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

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
