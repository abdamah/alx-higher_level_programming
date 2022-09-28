#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list"""
    if not my_list:
        return my_list
    return [value if value != search else replace for value in my_list]
