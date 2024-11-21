#!/usr/bin/python3
"""Module defining a Square class with size,
position, area, and printing functionality"""


class Square:
    """Class defining a square with private
    size and position attributes, area, and printing"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute with validation"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value)
        or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square with the character '#' at the given position"""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
