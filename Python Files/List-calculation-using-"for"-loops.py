years=[0,1,2,3,4,5,6,7,8,9,10]
r=5.0
P= 100.0
for n in years:
    A=P*(1+r/100)**n
    print("Year",n,"    ""A =$%.2f" %A)