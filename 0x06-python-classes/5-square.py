#!/usr/bin/python3
"""Print the square of a number with the '#' sign"""


class Square:
    """initialise and print the square of a number"""
    def __init__(self, size=0):
        """initialize the side of the square"""
        self.size = size
    @property
    def size(self):
        """To retrieve the side of the square"""
        return self.__size
    @size.setter
    def size(self, value):
        """set the side of a square"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""
        area = self.__side * self.__side
        return area

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for item in range(self.__size):
                for num in range(self.__size):
                    print("#", end="")
                print()
