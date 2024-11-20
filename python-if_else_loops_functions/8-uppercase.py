#!/usr/bin/python3
from 8-uppercase import uppercase

uppercase("holberton")
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print("{}".format(uppercase_char), end="")
    print()
