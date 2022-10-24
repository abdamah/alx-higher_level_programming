#!/usr/bin/python3

"""Defines lookup function."""


def lookup(obj):
    """Return list of available attributes and methods of an object"""
    return (dir(obj))
