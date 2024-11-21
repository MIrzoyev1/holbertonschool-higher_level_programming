#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of
            the square. Defaults to (0, 0).
        """
        self._size = size
        self._position = position

    @property
    def size(self):
        """Getter method for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size attribute with type and value validation.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position attribute with type and value validation.

        Args:
            value (tuple): A tuple of two positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters, respecting position."""
        if self.__size == 0:
            print()
            return

        # Print vertical spacing based on position[1]
        for _ in range(self.__position[1]):
            print()

        # Print the square
        for _ in range(self.__size):
            # Print horizontal spacing based on position[0]
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
