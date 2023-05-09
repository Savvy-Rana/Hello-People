# Sawera Ashfaq
# Using the function range to loop over indices

r=5.0
P=100
N=10
for n in range(N+1):
    A=P*(1+r/100)**n
    print("Year #",n,"is " "$%.2f" %A)
