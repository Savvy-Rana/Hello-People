# Sawera Ashfaq 
# Function with multiple parameters in ()

def amount(P,r,n):
    return P*(1+r/100)**n
a1=amount(100,5.0,10)
a2=amount(P=100, r=5.0, n=10)
print("$%.2f" %a1,"\n" "$%.2f" %a2)