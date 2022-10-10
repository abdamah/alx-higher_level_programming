#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Function that prints a function safely."""
    try:
        func = fct(*args)

    except Exception as err:
        func = None
        sys.stderr.write("Exception: {}\n".format(err))

    return (func)
