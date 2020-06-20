#Coding_Resources
#!/usr/bin/env python
def table(num):
	count = 1
	while(count<11):
		print(str(num)+" * "+str(count)+" = "+str(count*num)+"\n")
		count = count+1
		
print("Enter a number to find its multiplication table")
num = int(input())
table(num)
