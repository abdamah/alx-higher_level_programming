#!/usr/bin/python3
""" Magic module """
import math


class MagicClass:
    """ Magic class"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """ AREA """
    def area(self):
        """Define Circle area"""
	return (math.pi * self.__radius ** 2)

    """ Define Circle Circumfrence """
    def circumference(self):
        return (2 * math.pi * self.__radius)
