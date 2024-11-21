#!/usr/bin/python3
"""Module defining a Square class with size,
area, and printing functionality"""


class Square:
    """Class that defines a square with private size
    attribute and methods for area and printing"""

    def __init__(self, size=0):
        """Initialize the square with size"""
        self.size = size

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square with the character '#'"""
        if self.size == 0:
            print()  # If size is 0, print an empty line
        else:
            for i in range(self.size):
                print("#" * self.size)
