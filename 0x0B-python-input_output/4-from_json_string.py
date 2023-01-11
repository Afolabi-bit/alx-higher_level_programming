#!/usr/bin/python3
"""
This module returns an object represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str: str to be converted
    Return: the Python object representation
    of a JSON string
    """
    return json.loads(my_str)
