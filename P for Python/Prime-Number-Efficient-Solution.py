#!/usr/bin/env python
#Coding_Resources

""" Prime number - Check whether the input number is prime or not. """
__author__      = "Kaushik-Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def isPrimeEfficientSolution(n):
    if n == 1:
        return False
    if  n == 2 or n == 3:
        return True
    if n %2 == 0 or n%3 == 0:
        return False

    i = 5
    while (i*i<=n):
        if n%i == 0 or n %(i+2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    print(isPrimeEfficientSolution(int(input("Enter a number:- "))))

    
