#Coding_Resources  

#!usr/bin/env python
print("Enter a number to check for positive or not")
num = int(input())
if num>0:
	print("The number "+str(num)+" entered is Positive")	#Converting the int data type to string
elif num<0:
	print("The number"+str(num)+ " you have entered is Negative")	#Converting the int data type to string
else:
	print("The number you have entered is 0")
