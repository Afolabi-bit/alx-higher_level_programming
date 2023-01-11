#!/usr/bin/python3
"""
This module defines a function that writes an Object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: object
        filename: text fileto write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
