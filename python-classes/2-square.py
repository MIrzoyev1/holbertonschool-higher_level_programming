#!/usr/bin/python3
"""Module defining a Square class"""


class Square:
    """Class that defines a square with private size attribute"""

    def __init__(self, size=0):
        """Initialize the square with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
