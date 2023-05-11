#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    argv = sys.argv
    num = len(sys.argv) - 1
    if num == 0:
        print(f"{0}: argument.")
    elif num >= 1:
        print(f"{num} arguments:")
        while(i < len(sys.argv)):
            print(f"{i}: {argv[i]}")
            i += 1
