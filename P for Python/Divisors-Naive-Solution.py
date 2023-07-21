#!/usr/bin/env python
#Coding_Resources
""" Divisors of a number - Print divisors of the given number. """
__author__      = "Kaushik Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def naiveDivisors(n):  
  for i in range(1,n+1):
    if n%i==0:
      print(i)
      
if __name__ == "__main__":
  naiveDivisors(int(input("Enter a number:-\t")))
