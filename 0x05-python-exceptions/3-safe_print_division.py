#!/usr/bin/python3
def safe_print_division(a, b):
    """Try catch finaly statement"""
    try:
        c = a / b

    except (TypeError, ZeroDivisionError, ValueError):
        c = None

    finally:
        print("Inside result: {}".format(c))

    return (c)
