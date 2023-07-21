#!/usr/bin/env python
#Coding_Resources
""" Find the factors of the given input number """
__author__      = "Kaushik Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def factorial(num):
                print("The factorial of the number is: ")
                fact = 1
                i = 1
                for i in range(1,num+1):
                        
                        if i<=num:
                                fact = fact * i
		print(fact)


if __name__ == "__main__":
	num = int(input("Enter a number to calculate the factorial   "))
	fact = factorial(num)

        

