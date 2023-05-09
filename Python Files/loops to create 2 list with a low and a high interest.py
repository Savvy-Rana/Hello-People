

# Sawera Ashfaq
# Using the loops to create 2 list with a low and a high interest!

P=100
rlow=2.5
rhigh=5.0
N=10
Alow=[]
Ahigh=[]
for n in range(N+1):
    A=P*(1+rlow/100)**n
    Alow.append("$%.2f" %A)
    A=P*(1+rhigh/100)**n
    Ahigh.append("$%.2f" %A)
for i in range(len(Alow)):
    print(Alow[i],"\t",Ahigh[i])