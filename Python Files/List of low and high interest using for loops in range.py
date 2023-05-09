
# Sawera Ashfaq
# Using the loops to create a list with high and low interest rate

rlow=2.5
rhigh=5.0
P=100
N=10
A_high=[]
A_low=[]
for n in range(N+1):
    Alow=P*(1+rlow/100)**n
    A_low.append("$%.2f" %Alow)
    Ahigh=P*(1+rhigh/100)**n
    A_high.append("$%.2f" %Ahigh)
print("This is the list with r=2.5(low):",A_low)
print("This is the list with r=5.0(high):", A_high)
