#Sawera Ashfaq  
# Function returning multiple arguments

def f(x):
    return x, x**2,x**4
a=f(2)
print(type(a),a)

a1,a2,a3=a
print(a1,a2,a3)