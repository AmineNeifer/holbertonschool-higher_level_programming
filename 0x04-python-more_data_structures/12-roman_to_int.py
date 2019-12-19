#!/usr/bin/python3
def roman_to_int(roman_string):
    ad = {'M': 1000}
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    numerals.update(ad)
    result = 0
    if type(roman_string) == str:
        for i in range(len(roman_string)):
            if roman_string[i] not in numerals:
                return (0)
            if i < len(roman_string) - 1:
                i2 = numerals[roman_string[i+1]]
                i1 = numerals[roman_string[i]]
            if i < len(roman_string) - 1 and i2 > i1:
                result -= numerals[roman_string[i]]
            else:
                result += numerals[roman_string[i]]
        return (result)
    else:
        return (0)
