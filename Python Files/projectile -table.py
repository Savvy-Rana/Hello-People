#Sawera Ashfaq
#02/13/23
#projectile motion -table
from math import sin,cos,pi 
vo=50   #initical speed of the ball (m/s)
g=9.81  #gravity (m/s^2)
theta=45    #angle of the ball (degrees)
t=0   #time of the ball(s)
y=0     #height of the ball (m)
print ("time\theight\tdistance")
while y>=0:
    y=vo*sin(theta*pi/180)*t-0.5*g*t**2
    x=vo*t*cos(theta*pi/180)
    print ("%.2f" %t, "\t%.2f" %y, "\t%.2f" %x)
    t=t+0.1