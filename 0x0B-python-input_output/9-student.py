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
	self.last_name = lst_name
        self.age = age

    def to_json(self):
        """ Dict representation of Student """
        return self.__dict__
