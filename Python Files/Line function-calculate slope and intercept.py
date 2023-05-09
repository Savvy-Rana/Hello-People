# Sawera Ashfaq

def line(x0,y0, x1,y1):
    """ Calculate the coefficient a and b in the y=a*x+b  function for 
    a straight line, that goes through 2points:(x0,y0) and (x1,y1)
    """
    a=(y1-y0)/(x1-x0)
    b=y0-a*x0
    return a,b
a,b=line(3,3,6,8)
print(a,b)