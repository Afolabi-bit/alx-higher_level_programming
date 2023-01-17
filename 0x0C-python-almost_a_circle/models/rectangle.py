#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits
from Base (base.py)
"""
from models.base import Base


class Rectangle(Base):
    """ Defines a Rectangle that inherits
        from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation of Rectangle class """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
