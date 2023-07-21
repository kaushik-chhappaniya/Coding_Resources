#!/usr/bin/env python
#Coding_Resources
""" Find the given power of the given number - Naive Solution. """
__author__      = "Kaushik Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def naiveSolution(num,pow):
  x = 1
  for i in range(pow):
    x = x*num
    return x

if __name__ == "__main__":
  naiveSolution(*map(int,input("Enter number and to the power separated by space :\t").split()))
  
