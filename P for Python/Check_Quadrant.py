#Coding_Resources

#!/usr/bin/env python
def check(x,y):
  if x>0 and y>0:
  	print("The point ("+str(x)+","+str(y)+") is in the First Quadrant")
  	
  elif x<0 and y>0:
  	print("The point ("+str(x)+","+str(y)+") is in the Second Quadrant")
  
  elif x<0 and y<0:
  	print("The point ("+str(x)+","+str(y)+") is in the Third Quadrant")
  	
  elif x>0 and y<0:
  	print("The point ("+str(x)+","+str(y)+") is in the Fourth Quadrant")



x = input("Enter the value of X coordinate\n")
y = input("Enter the value of Y coordinate\n")
check(x,y)
