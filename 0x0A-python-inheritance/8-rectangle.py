#!/usr/bin/python3
"""
This module defines a Rectangle class that
inherits from BaseGeometry (7-base_geometry.py)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rect class """
    def __init__(self, width, height):
        """ Instantiation of Rectangle class """
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
