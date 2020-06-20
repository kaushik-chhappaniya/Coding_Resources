#Coding_Resources

#!/usr/bin/env python
def check_triangle(x,y,z):
  if x+y>z and x+z>y and y+z>x:
    print("The triangle of the given size exsists")
  else:                                 
    print("The triangle does not exist")


print("Enter length of the triangle")
x = float(input("X = "))
y = float(input("Y = "))
z = float(input("Z = "))
check_triangle(x,y,z)
