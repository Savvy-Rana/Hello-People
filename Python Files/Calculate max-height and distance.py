#Sawera Ashfaq
#02/13/23
#projectile motion -max height-max distance
print("Lets Calculate the max height and distanc using speed at 45 degree:")
from math import sin,cos,pi 
vo=int(input("Please enter the initial speed:"))   #initical speed of the ball (m/s)
g=9.81  #gravity (m/s^2)
theta=45    #angle of the ball (degrees)
t=0   #time of the ball(s)
y=0     #height of the ball (m)
ymax=0 #initial y max height of the ball 
xmax=0  #initial x max distance of the ball 
tymax=0 #initial max heigt time 
txmax=0 #initial max distance time 
while y>=0:
    y=vo*sin(theta*pi/180)*t-0.5*g*t**2
    x=vo*t*cos(theta*pi/180)
    if y>=ymax:
        ymax=y
        tymax=t
    if x>=xmax:
        xmax=x
        txmax=t
    t=t+0.1
print ("Max height %0.2f" %ymax,"(m)")
print ("Max height time %0.2f" %tymax,"(s)")
print ("Max distance %0.2f" %xmax,"(m)")
print ("Max distance time %0.2f" %txmax, "(s)")
