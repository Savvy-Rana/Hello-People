#Python Practice 
#By- Sawera Ashfaq 

#Ex-1
#How to Calculate distance between 2 cities.

import math

x1=int(input("Enter the X coordinate of the 1st city: "))
y1=int(input("Enter the Y coordinate of the 1st city: "))
x2=int(input("Enter the X coordinate of the 2nd city:"))
y2=int(input("Enter the Y coordinate of the 2nd city:"))

d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f'The distance between the 1st city and 2nd city is {d}')

