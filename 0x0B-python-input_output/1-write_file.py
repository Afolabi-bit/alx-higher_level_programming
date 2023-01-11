#!/usr/bin/python3
"""
This module defines a function that writes a
string to a text file (UTF8) and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """ Write text to file"""
    with open(filename, encoding="utf-8") as f:
        f.write(text)
