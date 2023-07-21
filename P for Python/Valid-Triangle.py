#!/usr/bin/env python
#Coding_Resources
""" Check if the given 3 values belong to a valid triangle """
__author__      = "Kaushik Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def check_triangle(x,y,z):
  if x+y>z and x+z>y and y+z>x:
    print("The triangle of the given size exsists")
  else:                                 
    print("The triangle does not exist")


if __name__ == "__main__":
  print("Enter length of the triangle")
  x = float(input("X = "))
  y = float(input("Y = "))
  z = float(input("Z = "))
  check_triangle(x,y,z)
