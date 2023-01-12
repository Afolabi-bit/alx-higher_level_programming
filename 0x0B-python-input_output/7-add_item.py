#!/usr/bin/python3
"""
This module defines functions that
loads from JSON,
saves to JSON, and
adds all arguments
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    Adds all arguments to a python list
    """
    filename = "add_item.json"
    num = len(sys.argv)
    try:
        arg_list = load_from_json_file(filename)
    except FileNotFoundError:
        arg_list = []

    for i in range(1, num):
        arg_list.append(sys.argv[i])

    save_to_json_file(arg_list, filename)


add_item()
