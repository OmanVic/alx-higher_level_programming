#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    screen = sys.argv
    result = 0
    leng = len(screen)
    i = 1
    while(i < leng):
        result += int(screen[i])
        i += 1
    print(f"{result}")
