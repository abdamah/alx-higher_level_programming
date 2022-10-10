#!/usr/bin/python3
def magic_calculation(a, b):
    """Magic function with try-catch block."""
    c = 0
    for num in range(1, 3):
        try:
            if (num > a):
                raise Exception('Out of range.')
            else:
                c += a ** b / num
        except:
            c = a + b
            pass
    return (c)
