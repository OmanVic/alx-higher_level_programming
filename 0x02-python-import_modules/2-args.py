#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    arg = 'arguments'
    argv = sys.argv
    num = len(sys.argv) - 1
    if num == 0:
        print(f"{0} arguments.")
    elif num >= 1:
        if num == 1:
            arg = 'argument'
        print(f"{num} {arg}:")
        while(i < len(sys.argv)):
            print(f"{i}: {argv[i]}")
            i += 1
