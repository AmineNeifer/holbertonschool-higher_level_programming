#!/usr/bin/python3
def weight_average(my_list=[]):
    divi = 0
    sumi = 0
    if len(my_list) == 0:
        return (0)
    for i in my_list:
        sumi += i[0]*i[1]
        divi += i[1]
    return (sumi / divi)
