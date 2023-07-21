#!/usr/bin/env python
#Coding-Resources
"""
Power function efficient solution - Calculate the given power of the number.
Time complexity - BIGO(logn) 
Auxiliary space complexity - BIGO(logn)
"""
__author__      = "Kaushik-Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def powerEfficient(num,pow):
  if pow == 0:
    return 1
  temp = powerEfficient(num , pow//2)  #floor division
  temp *= temp
  if pow%2==0:
    return temp
  else:
    return temp*num

if __name__ == "__main__":
  print(powerEfficient(*map(int,input("Enter number and to the power separated by space :\t").split())))
