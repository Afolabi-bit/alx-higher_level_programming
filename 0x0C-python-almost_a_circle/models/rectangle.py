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
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, w):
        """ width setter """
        self.width = w

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, h):
        """ height setter """
        self.height = h

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.__y = y
