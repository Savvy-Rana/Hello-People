years=[0,1,2,3,4,5]
for n in years:
    r=5.0
    P=100
    A=P*(1+r/100)**n
    print("Year #",n,"is " "$%.2f" %A)