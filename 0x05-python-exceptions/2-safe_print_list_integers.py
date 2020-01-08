#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    t = 0
    try:
        for i in range(x):
            if (type(my_list[i]) is int):
                print("{:d}".format(my_list[i]), end="")
                t = t + 1
        print()
    except:
        return(t)
    return(t)
