#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for item in range(x):
        try:
            print(my_list[item], end="")
            n += 1
        except IndexError:
            print()
            return n
    print()
    return n
