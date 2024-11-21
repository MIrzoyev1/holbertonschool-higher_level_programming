#!/usr/bin/python3
s1 = Square()
print(s1.area())

s2 = Square(4)
print(s2.area())

s2.size = 5
print(s2.area())

try:
    s3 = Square(-3)
except ValueError as e:
    print(e)

try:
    s4 = Square("size")
except TypeError as e:
    print(e)
