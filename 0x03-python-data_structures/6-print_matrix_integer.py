#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for item in lists:
            print("{}".format(item), end="")
        print("")
