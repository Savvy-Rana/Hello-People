
from math import sqrt 
def getcoefficient():
    print("Solving Quadratic Equation: ax**2+bx+c=0") 
    a, b, c = eval(input("Please enter the a, b, c coefficients: ")) 
    int(a), int(b), int(c) 
    return a,b,c
def getdisc(a,b,c):
    disc = b*b-4*a*c 
    return disc
def decision(disc):
    if disc > 0: 
        x1 = (-b+sqrt(disc))/(2*a) 
        x2 = (-b-sqrt(disc))/(2*a) 
        print("The roots of the equation are:", x1, x2) 
    elif disc==0: 
        x1 = (-b)/(2*a) 
        x2 = (-b)/(2*a) 
        print("The roots of the equation are equal:", x1, 'and', x2) 
    else: 
       v = -b/(2*a) 
       w = sqrt(-disc)/(2*a) 
       print("The first root is:", v,"+j","%0.2f"%w) 
       print("The second root is:", v,"-j",'%0.2f' %w) 

a,b,c=getcoefficient()
disc=getdisc(a,b,c)
decision(disc)

    