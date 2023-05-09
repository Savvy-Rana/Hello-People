

# Sawera Ashfaq
# Using the for loop , with "low,high zip" to print 

P=100
rlow=2.5
rhigh=5.0
N=10
Alow=[P*(1+rlow/100)**n for n in range(N+1)]
Ahigh=[P*(1+rhigh/100)**n for n in range(N+1)]
for low,high in zip(Alow,Ahigh):                    #***low,high zip
    print("Low $%.2f"%low,"\t High $%.2f"%high)








#for i in range(len(Alow)):
    #print("%.2f" %Alow[i], "%.2f" %Ahigh[i])
    
    