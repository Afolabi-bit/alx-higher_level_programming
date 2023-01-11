#!/usr/bin/python3
"""
This module defines a function that reads a
text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    with open(filename) as f:
        f.read()
