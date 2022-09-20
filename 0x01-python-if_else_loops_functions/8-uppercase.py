#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ascii_number = ord(i)
        if ascii_number in range(97, 123):
            ascii_number = ascii_number - 32
        print("{:c}".format(ascii_number), end="")
    print()
