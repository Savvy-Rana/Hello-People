
# How to create an empty list and fill it with data -using formula to calculate. 

P=100.0
r=5.0
N=10
amount=[]                  #Started with an empty list
for n in range(N+1):
    A=P*(1+r/100)**n       # Used formula to calculate the data
    amount.append("%.2f" %A)   # A is 2 decimal places
print(amount)