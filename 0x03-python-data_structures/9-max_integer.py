#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for item in my_list:
        if my_list[0] < item:
            my_list[0] = item
    return my_list[0]
