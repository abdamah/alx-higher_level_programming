#!/usr/bin/python3
def roman_to_int(roman_string):
    """ converts a Roman numeral to an integer."""
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    number = len(roman_string)
    int_value = romans[roman_string[number-1]]
    for i in range(number - 1, 0, -1):
        curr_value = romans[roman_string[i]]
        prev_value = romans[roman_string[i-1]]

        if prev_value >= curr_value:
            int_value += prev_value
        else:
            int_value -= prev_value

    return int_value
