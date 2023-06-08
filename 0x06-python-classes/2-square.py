#!/usr/bin/python3
""" defining a square by its sides"""


class Square:
    """representing a square with a given size"""


    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
