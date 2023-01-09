#!/usr/bin/python3
"""
This module defines a method which creates
a class MyList that inherits from list
"""


class MyList(list):
    """
        A subclass of list
    """
    def __init__(self):
        super().__init__()
    def print_sorted(self):
        sort = sorted(self)
        print(sort)
