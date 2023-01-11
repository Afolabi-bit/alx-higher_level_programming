#!/usr/bin/python3
"""
This module defines a function that returns
the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: dictionary
    """
    return json.dumps(my_obj)
