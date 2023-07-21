#!/usr/bin/env python
#Coding_Resources
""" Check Quadrants based on two numbers """
__author__      = "Kaushik-Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def check(x,y):
  if x>0 and y>0:
  	print("The point ("+str(x)+","+str(y)+") is in the First Quadrant")
  	
  elif x<0 and y>0:
  	print("The point ("+str(x)+","+str(y)+") is in the Second Quadrant")
  
  elif x<0 and y<0:
  	print("The point ("+str(x)+","+str(y)+") is in the Third Quadrant")
  	
  elif x>0 and y<0:
  	print("The point ("+str(x)+","+str(y)+") is in the Fourth Quadrant")



if __name__ == "__main__":
  x = input("Enter the value of X coordinate\n")
  y = input("Enter the value of Y coordinate\n")
  check(x,y)
