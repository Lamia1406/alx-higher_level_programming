#!/usr/bin/python3
""" this module consists only of one function: lookup(obj)"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
