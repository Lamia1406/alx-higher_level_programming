#!/usr/bin/python3
""" this module consists only of one function: lookup(obj)"""


class MyList(list):
    """class that inherits from a list"""
    def print_sorted(self):
        """prints the list but sorted"""
        print(sorted(self))
