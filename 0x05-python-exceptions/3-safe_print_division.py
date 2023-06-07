#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        n = a / b
        print("Inside result: {}".format(n))
        return n
    except ZeroDivisionError:
        n = None
        print("Inside result: {}".format(n))
        return n
