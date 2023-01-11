#!/usr/bin/python3
"""
This module defines a function that writes a
string to a text file (UTF8) and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """ Write text to file
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Return:
        The number of characters written.
    """
    with open(filename, w, encoding="utf-8") as f:
        return f.write(text)
