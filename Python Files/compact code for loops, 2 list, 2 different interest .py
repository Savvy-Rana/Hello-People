

# Sawera Ashfaq
# Using the loops to create 2 list with a low and a high interest in a compact code

P=100
rlow=2.5
rhigh=5.0
N=10
Alow=[P*(1+rlow/100)**n for n in range(N+1)]
Ahigh=[P*(1+rhigh/100)**n for n in range(N+1)]

print(Alow)
print(Ahigh)

for i in range(len(Alow)):
    print("%.2f" %Alow[i], "%.2f" %Ahigh[i])
    
    