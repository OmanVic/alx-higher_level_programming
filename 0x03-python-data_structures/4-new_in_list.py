#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_copy = []
    i = 0
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for item in my_list:
            if i == idx:
                item = element
            new_copy.append(item)
            i += 1
        return new_copy
