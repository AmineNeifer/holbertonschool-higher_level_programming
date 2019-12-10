#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if (j == 9 and i == 8):
            print("89")
        elif (j > i):
            print("{}{}, ".format(i, j), end="")
