# Sawera Ashfaq
# Default value

def yfunc(t,vo=5, g=9.81):
    y=vo*t-0.5*g*t**2
    dydt=vo-g*t
    return y,dydt
y1, dydt1=yfunc(0.2)            # 0.2 is new value, for vo and g dafault values used
y2, dydt2=yfunc(0.2, vo=7.5)    #0.2 and 7.5 is new value, g is dafault
y3,dydt3=yfunc(0.2,7.5,10)      # all the value are new - no default value
print(y1,dydt1)
print(y2,dydt2)
print(y3,dydt3)