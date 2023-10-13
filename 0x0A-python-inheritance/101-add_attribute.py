#!/usr/bin/python3
""" this module consists only of one function :
        add_attribute(obj, attr, val)"""


def add_attribute(obj, attribute, value):
    """adds an attribute to  class
    Args:
        obj: the object we want to add the attribute to
        attribute: the attribute to add
        value: the value to be affected to the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
