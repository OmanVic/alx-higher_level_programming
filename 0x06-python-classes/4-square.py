#!/usr/bin/python3
"""accesing and updating private attributes"""


class Square:
    """defining the properties of a square"""

    def __init__(self, size):
        """initialize a square.

        Args:
            size (int): the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """return the private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of a private attribute"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return the current square area"""

        area = self.__size * self.__size
        return area
