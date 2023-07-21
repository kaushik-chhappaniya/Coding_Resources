#!/usr/bin/env python
#Coding_Resources
""" Divisors of a number - Print divisors of the given number with an efficient solution. """
__author__      = "Kaushik Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def divisorsOptimised(n):
  i=1
  while(i*i<n):
    if n%i==0:
      print(int(i))
    i+=1
  while(i>=1):
    if n%i==0:
      print(int(n/i))
    i-=1

if __name__ == "__main__":
  divisorsOptimized(int(input("Enter a number:\t")))
