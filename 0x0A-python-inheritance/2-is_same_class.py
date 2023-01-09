#!/usr/bin/python3
"""
This module defines a function that checks if
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ Return a bool """
    return (type(obj) == a_class)
