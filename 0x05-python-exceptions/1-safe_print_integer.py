#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format()"""
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return (False)

    return (True)
