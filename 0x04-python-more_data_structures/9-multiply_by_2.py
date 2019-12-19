#!/usr/bin/python3
def multiply_by_2(a_dictionary):
        new_dict = a_dictionary.copy()
        for val in a_dictionary:
            new_dict[val] = a_dictionary[val] * 2
        return(new_dict)
