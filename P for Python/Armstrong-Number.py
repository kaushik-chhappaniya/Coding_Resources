#!/usr/bin/env python
#Coding_Resources
""" Check whether the given number is Artmstrong or not """
__author__      = "Kaushik-Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def Armstrong(num):
	temp = num
	rem = add = cube = 0
	while(temp!=0):
	  rem = temp%10
	  cube = rem*rem*rem
	  add = add + cube
	  temp = temp/10
	if add == num:
	  print("The number is armstrong number")
	else: 
	  print("The number is not a Armstrong number")


if __name__ == "__main__":
	print("Enter a number to check whether it is Armstrong or not")
	num = int(input())
	Armstrong(num)
	#Armstrong numbers are:0, 1, 153, 370, 371,407
