# Sawera Ashfaq 
# Function to return more than one value 

P=100
r=5.0
def amount(n,r):
    r=r-1.0
    a=P*(1+r/100)**n
    return a,r
a,b=amount(7,5)
print("$%.2f" %a,b)
print(r)