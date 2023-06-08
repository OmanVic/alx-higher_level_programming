#!/usr/bin/python3
"""accesing and updating private attributes"""


class Square:
    """defining the properties of a square"""
    def __init__(self, size):
        self.size = size
    @property
    def size(self):
        """return the private attribute"""
        return self.__size
    @size.setter
    def size(self, value):
        """Set the size of a private attribute"""
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """calculate the area"""

        area = self.__size * self.__size
        return area
