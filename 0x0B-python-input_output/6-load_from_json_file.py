#!/usr/bin/python3
"""
This module defines a function that creates an
Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename: name of file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.load(f)