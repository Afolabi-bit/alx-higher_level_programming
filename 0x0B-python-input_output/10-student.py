#!/usr/bin/python3
"""
Defines a class Student
"""


class Student():
    """ Student """
    def __init__(self, first_name, last_name, age):
        """ Initialize a new Student
        Args:
            first_name (str): The first name of Student
            last_name (str): The last name of Student
            age (int): age of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dict representation of Student
            If attrs is a list of strings,
	    represents only those attributes included in the list.
            Args:
                attrs (list): attribute
        """
        if (type(attrs) == list and
			all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
