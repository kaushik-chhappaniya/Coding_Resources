#Coding_Resources

#!/usr/bin/env python

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



print("Enter a number to check whether it is Armstrong or not")
num = int(input())
Armstrong(num)

#Armstrong numbers are:0, 1, 153, 370, 371,407
