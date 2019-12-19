#!/usr/bin/python3
def best_score(a_dictionary):
    maax = 0
    if (a_dictionary):
        for val in a_dictionary:
            if maax <= a_dictionary[val]:
                maax = a_dictionary[val]
                maxy = val
        return (maxy)
    else:
        return (None)
