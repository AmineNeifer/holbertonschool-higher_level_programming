#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        test = 0
        for z in reversed(range(i)):
            if my_list[i] == my_list[z]:
                test = 1
        if test == 0:
            new_list.append(my_list[i])
    summ = 0
    for x in new_list:
        summ += x
    return (summ)
