#!/usr/bin/python3
"""
This is a module containing the function
lookup which returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
        obj - an object
    """
    return dir(obj)
