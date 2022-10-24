#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """ My int inherits from int """
    def __eq__(self, value):
        """ Function for equals """
        return(int(self) != int(value))

    def __ne__(self, value):
        """ Function for not equals """
        return (int(self) == int(value))
