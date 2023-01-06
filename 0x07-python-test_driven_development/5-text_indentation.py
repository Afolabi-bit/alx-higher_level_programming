#!/usr/bin/python3
"""
A module that checks for indentation
after certain characters
"""


def text_indentation(text):
    """
	    text: expected string input
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    check = 0
    for c in text:
        if check == 0:
            if c == ' ':
                continue
            else:
                check = 1
        if check == 1:
            if c == '.' or c == '?' or c == ':':
                print(c)
                print()
            else:
                print(c, end="")
