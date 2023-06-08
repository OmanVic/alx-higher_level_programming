#!/usr/bin/python3
"""Find the area of a square"""


class Square:
    """define the properties of a square"""

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate the area of a square"""
        area = self.__size * self.__size
        return area
