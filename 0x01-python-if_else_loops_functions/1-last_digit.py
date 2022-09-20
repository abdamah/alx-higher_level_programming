#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = number % (-10)
if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")

if lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")

elif lastdigit < 6 != 0:
    print(f"Last digit of {number} is {lastdigit} and is less than 6 and not 0")
