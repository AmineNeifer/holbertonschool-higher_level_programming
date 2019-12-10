#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if(number < 0):
    n = (number % 10) - 10
else:
    n = number % 10

print("Last digit of ", end="")

if(n > 5):
    print("{} is {} and is greater than 5".format(number, n))
elif(n == 0):
    print("{} is {} and is 0".format(number, n))
else:
    print("{} is {} and is less than 6 and not 0".format(number, n))
