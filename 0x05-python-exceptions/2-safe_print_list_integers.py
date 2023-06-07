#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for item in range(x):
        try:
            nitem = my_list[item]
            nitem = int(nitem)
            print("{:d}".format(nitem), end="")
            n += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print()
    return n
