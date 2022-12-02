#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    a = 0
    for i in my_list:
        if i >= a:
            a = i
        else:
            continue
    return a
