#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) < 123):
            n = ord(str[i]) - 32
        else:
            n = ord(str[i])
        print(chr(n), end="")
    print()
