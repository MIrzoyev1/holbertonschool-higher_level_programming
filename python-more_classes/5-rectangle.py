#!/usr/bin/python3
''' Class Rectangle that defines a rectangle
'''

class Rectangle:
    ''' Rectangle class with properties
    '''

    def __init__(self, width=0, height=0):
        ''' Initialize a new Rectangle object.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' Getter for the width of the rectangle.
        
        Returns:
            int: The current width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Setter for the width of the rectangle.

        Args:
            value (int): The value to set the width to.
        
        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' Getter for the height of the rectangle.
        
        Returns:
            int: The current height of the rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Setter for the height of the rectangle.

        Args:
            value (int): The value to set the height to.
        
        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        '''
        return self.__width * self.__height

    def perimeter(self):
        ''' Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
            If either the width or height is 0, returns 0.
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        ''' Return a string representation of the rectangle.

        Returns:
            str: A string containing a visual representation of the rectangle
                 using "#" characters. If either width or height is 0, returns an empty string.
        '''
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        ''' Return a string representation of the rectangle for debugging.

        Returns:
            str: A string representing the rectangle in the form of
                 "Rectangle(width, height)".
        '''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        ''' Destructor for the Rectangle class. Prints a message when the rectangle is deleted.
        
        Prints:
            "Bye rectangle..."
        '''
        print("Bye rectangle...")

