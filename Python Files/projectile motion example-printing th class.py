#Sawera Ashfaq  
# Projectile motion- multiple return values based on multiple parametes
# Pay attention*** ----> multiple "return values" are returned as tuples

#  Height of an object in verticle motion  ==>  y(t)=(vo)(t)-(0.5)*g*t**2
#  Speed of object in verticle motion --> take dydt(derivative) of the y function

def yfunction(vo,t):
    g=9.81
    y=vo*t-0.5*g*t**2          #height
    dydt=vo-g*t                     #speed
    return y, dydt
t= yfunction(30,2)
print(t)
print(type(t))
    