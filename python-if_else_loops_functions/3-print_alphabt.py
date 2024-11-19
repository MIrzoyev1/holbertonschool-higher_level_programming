#!/usr/bin/python3

for i in range(97, 123):  # ASCII range for lowercase letters
    if i != 113 and i != 101:  # Exclude 'q' (113) and 'e' (101)
        print("{}".format(chr(i)), end="")   
