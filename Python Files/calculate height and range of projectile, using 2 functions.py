# Sawera Ashfaq
# Python Program to calculate height and range of projectile, using 2 functions.

from math import sin,cos,pi

g=9.81
tymax=0.0
txmax=0.0

def maxheight(vo,theta):
    ymax=0.0
    t=0.0
    while True:
        y=vo*sin(theta*pi/180)*t-0.5*g*t**2
        if y>=ymax:
            ymax=y
            tymax=t
        elif y<0:
            break
        t+=0.1
    return tymax, ymax

def maxrange(vo,theta):
    xmax=0.0
    t=0.0
    while True:
        x=vo*cos(theta*pi/180)*t
        y=vo*sin(theta*pi/180)*t-0.5*g*t**2
        if y<0:
            break
        elif x>=xmax:
            xmax=x
            txmax=t
        t+=0.1
    return txmax, xmax

txmax,xmax=maxrange(50,45)
tymax,ymax=maxheight(50,45)

print("The max range is %.2f" %xmax,"[m] in %.2f" %txmax,"[s].")
print("The max height is %.2f" %ymax,"[m] in %.2f" %tymax, "[s].")

