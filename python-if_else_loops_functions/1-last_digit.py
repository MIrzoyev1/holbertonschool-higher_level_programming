#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = number % 10  

if number < 0:
    last_digit = -abs(last_digit)

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
Last digit of -98 is -8 and is less than 6 and not 0
Last digit of 98 is 8 and is greater than 5

