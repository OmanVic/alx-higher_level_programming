#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    order_list = list(set(my_list))
    for item in order_list:
        result += item
    return result
