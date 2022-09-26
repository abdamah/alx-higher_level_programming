#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds max integer of a given list of integers"""
    if len(my_list) == 0:
        return (None)

    maxi = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxi:
            maxi = my_list[i]
    return (maxi)
