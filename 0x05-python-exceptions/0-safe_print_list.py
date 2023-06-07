#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        my_list[x - 1]
    except IndexError:
        return
    else:
        for item in range(x):
            print(my_list[item], end="")
        print("")
        return x

