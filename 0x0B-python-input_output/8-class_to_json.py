#!/usr/bin/python3
"""
A function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """ obj: object """
    return obj.__dict__
