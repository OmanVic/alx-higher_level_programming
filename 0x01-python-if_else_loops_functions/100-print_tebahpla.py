#!/usr/bin/python3
for i in range(ord("z"), ord("a"), -2):
    print("{}{}".format(chr(i), chr(i-33)), end="")
