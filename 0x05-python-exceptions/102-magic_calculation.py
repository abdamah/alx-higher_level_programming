#!/usr/bin/python3
def magic_calculation(a, b):
    """Magic function with try-catch block."""
    result = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = a + b
            pass
    return (result)