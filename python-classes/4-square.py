#!/usr/bin/python3

# Assuming s1 and s2 are already defined as Square instances
s1 = Square()  # size = 0
s2 = Square(4)  # size = 4

# Print the area for s1 and s2
print(s1.area())  # Output: 0
print(s2.area())  # Output: 16

# Change size of s2
s2.size = 5
print(s2.area())  # Output: 25

# Try creating a square with invalid size (-3), which should raise an exception
try:
    s3 = Square(-3)  # This will raise a ValueError
except ValueError as e:
    print(e)  # This will print "size must be >= 0"

# Try creating a square with invalid size
("size"), which should raise a TypeError
try:
    s4 = Square("size")  # This will raise a TypeError
except TypeError as e:
    print(e)  # This will print "size must be an integer"
