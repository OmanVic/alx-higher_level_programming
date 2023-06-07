#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for item in my_list:
        try:
            if n < x:
                item = int(item)
                my_list[x-1]
                print("{:d}".format(item), end="")
                n += 1
        except ValueError:
            continue
        #except IndexError:
            #break
        #except TypeError:
            #continue
    print()
    return n
