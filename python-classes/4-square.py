#!/usr/bin/python3
"""Module defining a Square class with getter, setter, and area calculation"""


class Square:
    """Class defining a square with private size attribute and area method"""

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
