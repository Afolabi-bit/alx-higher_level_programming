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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns the JSON str of list_dictionary
            Args:
                list_dictionaries: list of dicts
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """
            Saves obj as json
        """
        filename = "{}.json".format(cls)
        obj_list = []

        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                obj_list.append(list_objs[i].to_dictionary())

            lists = cls.to_json_string(obj_list)
            with open(filename, "w") as f:
                f.write(lists)
