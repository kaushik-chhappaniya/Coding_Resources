#!/usr/bin/env python
#Coding_Resources
""" Prime number - Check whether the given input number is prime or not. """
__author__      = "Kaushik-Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"


def prime(num):
    if num == 1:
        return False
    i = 2
    while(i*i<=num):
        if num%i == 0:
            return False
        i += 1
        return True


if __name__ == "__main__":
    print(prime(int(input("Enter a number:-\n"))))
