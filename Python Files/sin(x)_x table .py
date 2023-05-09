#Sawera Ashfaq
#02/13/23
#sin(x)/x function table
from math import sin 
print ("x       sin(x)/x")
for x in range (-10,10):
    if x==0:
        y=1
    else:
        y=sin(x)/x
    print("%.2f" %x,"       %.2f" %y)
    