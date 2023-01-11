#!/usr/bin/python3
"""
This module appends a string to a file
"""


def append_write(filename="", text=""):
    """
    Args:
        filename: name of text file
        text: string to append
    Return:
        number o characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
