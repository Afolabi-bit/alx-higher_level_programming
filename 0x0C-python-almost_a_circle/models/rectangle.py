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

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        self.width = w

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        self.height = h

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y
