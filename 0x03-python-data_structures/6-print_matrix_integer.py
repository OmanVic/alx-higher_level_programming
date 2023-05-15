#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for lists in matrix:
        i = 0
        for item in lists:
            print("{:d}".format(item), end="")
            if i < len(lists) - 1:
                print(" ", end="")
                i += 1
        print("")
