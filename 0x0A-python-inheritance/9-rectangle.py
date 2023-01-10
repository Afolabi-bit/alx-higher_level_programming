#!/usr/bin/python3
"""
This module contains a class Rectangle that
inherits from BaseGeometry (7-base_geometry.py)
and is based on 8-rectangle.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rect class """
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the area of a rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """Str representation of rect """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
