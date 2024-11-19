#!/usr/bin/python3
def islower(c):
    letter = ord(c) 
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    elif letter in range(65, 90):
        return False
