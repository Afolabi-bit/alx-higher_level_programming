#!/usr/bin/python3
"""
This module adds two integer/float values
It return an integer value for the sum
"""

def add_integer(a, b=98):
    """a: int/float value
       b: int/float optional value
       Return: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
