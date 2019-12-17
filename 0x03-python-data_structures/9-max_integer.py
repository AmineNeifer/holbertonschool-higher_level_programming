#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi = 0
    for element in my_list:
        if maxi < element:
            maxi = element
    return maxi
