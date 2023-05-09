# Sawera Ashfaq 
# Global values and local values in functions difference

P=100
r=5.0
def amount(n):
    global r        # to override and make r= to the global value inside the loop for write <---
    r=4.0           # When we write global r it means from now on r= to whatever r value is inside loop
    return P*(1+r/100)**n
print("$%.2f" %amount(6))
print(r)