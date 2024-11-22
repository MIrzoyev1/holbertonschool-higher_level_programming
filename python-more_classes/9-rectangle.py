#!/usr/bin/python3
class Rectangle:
    # Public class attributes
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # Private instance attribute: width
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    # Private instance attribute: height
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    # Public instance method: area
    def area(self):
        return self.width * self.height

    # Public instance method: perimeter
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    # Print rectangle with the symbol
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    # Representation method for eval()
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    # Instance deletion message
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # Static method: bigger_or_equal
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    # Class method: square
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
