#!/usr/bin/python3
"""
This a module that defnes a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """ return a bool"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
