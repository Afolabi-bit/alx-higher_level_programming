#!/usr/bin/python3
"""
This module prints a function
"""


def print_square(size):
    """ size: size of square """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
