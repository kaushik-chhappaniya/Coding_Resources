#!/usr/bin/env python
#Coding_Resources
""" Check if the given year is a leap year or not """
__author__      = "Kaushik Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

print("Enter a year to check if it Leap year or not")
year = int(input())
if year%4 == 0:
	print("The year "+str(year)+" is a Leap year")
else: 
	print("The year "+str(year)+" is NOT a Leap year")

