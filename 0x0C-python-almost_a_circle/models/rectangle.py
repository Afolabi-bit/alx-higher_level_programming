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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, w):
        """ width setter """
        if type(w) is not int:
            raise TypeError("width must be an integer")
        elif w < 1:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, h):
        """ height setter """
        if type(h) is not int:
            raise TypeError("height must be an integer")
        elif h < 1:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Uses hashes to create rectangles"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """string representation of class"""
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y}'\
            f'- {self.__width}/{self.__height}'
