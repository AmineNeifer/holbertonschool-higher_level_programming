#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    t = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            t += 1
        if t > 0:
            print()
    except:
        if t > 0:
            print()
        return(t)
    return(t)
