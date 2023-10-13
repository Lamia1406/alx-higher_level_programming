#!/usr/bin/python3
""" this module consists only of one class: MyInt(int)"""


class MyInt(int):
    """class that inherits from int"""
    def __eq__(self, other):
        """returns the revert of =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """returns the revert of !="""
        return super().__eq__(other)
