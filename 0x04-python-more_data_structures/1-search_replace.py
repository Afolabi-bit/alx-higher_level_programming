#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    return list(i if i != search else replace for i in my_list)
