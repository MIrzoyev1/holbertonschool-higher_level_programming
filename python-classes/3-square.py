#!/usr/bin/python3
"""Module defining a Square class with area calculation"""


class Square:
    """Class that defines a square with
    private size attribute and area method"""

    def __init__(self, size=0):
        """Initialize the square with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square"""
        return self.__size ** 2
