#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for item in new:
        if new[item] == value:
            del a_dictionary[item]
    return a_dictionary
