#Sawera Ashfaq 
#solve quadratic equation by requeting a, b, and c and then display the solution x1 and x2

from math import sqrt 
print("Solving Quadratic Equation: ax**2+bx+c=0") 
a, b, c = eval(input("Please enter the a, b, c coefficients: ")) 
int(a), int(b), int(c) 
disc = b*b-4*a*c 
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
    
    
    
    