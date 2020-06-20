#Coding_Resources

#!/usr/bin/env python
def factorial(num):
                print("The factorial of the number is: ")
                fact = 1
                i = 1
                for i in range(1,num+1):
                        
                        if i<=num:
                                fact = fact * i
		print(fact)


num = int(input("Enter a number to calculate the factorial   "))
fact = factorial(num)

        

