#!/usr/bin/python3
"""
This module defines the base class for all other
classes in this package
"""
import json


class Base():
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
            Returns the JSON str of list_dictionary
            Args:
                list_dictionaries: list of dicts
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)
