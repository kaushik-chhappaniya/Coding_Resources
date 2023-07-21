#!/usr/bin/env python
#Coding_Resources
""" Print multiplication tables """
__author__      = "Kaushik Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

def table(num):
	count = 1
	while(count<11):
		print(str(num)+" * "+str(count)+" = "+str(count*num)+"\n")
		count = count+1

if __name__ == "__main__":
	print("Enter a number to find its multiplication table")
	num = int(input())
	table(num)
