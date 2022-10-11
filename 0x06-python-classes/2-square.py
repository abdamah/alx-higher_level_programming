#!/usr/bin/python3
"""square module that define Square class"""


class Square():
    """Square class with it's size and with validation"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size have to be an integer.")
        elif (size < 0):
            raise ValueError("size have to be equal to or greater than zero.")
        self.__size = size

