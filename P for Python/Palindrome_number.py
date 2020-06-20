#Coding_Resources

#!/usr/bin/env python
def palin(num):
	temp = num
	rem = rev = 0
	while(temp>0):	
		rem = temp%10
		rev =rev*10 + rem
		temp = temp//10
	if rev == num:
		return 1
	else:
		return 0
        
num = int(input("Enter a number to check palindrome or not   "))
if palin(num):
    print("The number is Palindrome  ")
else:
    print("The number is NOT palindrome " )



    
    
