#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dictionary = sorted(a_dictionary.items())
    for items, values in new_dictionary:
        print(f"{items}: {values}")
