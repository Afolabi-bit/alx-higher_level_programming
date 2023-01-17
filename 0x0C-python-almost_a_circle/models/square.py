#!/usr/bin/python3
"""
This module defines the Square class
which inherits from Rectangle(rectangle.py)
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class that defines a square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiation of variables """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """ size getter """
        return super().width

    @size.setter
    def size(self, width):
        """ size setter """
        self.width = width

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args is not None and len(args) > 0:
            attribute_list = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attribute_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
