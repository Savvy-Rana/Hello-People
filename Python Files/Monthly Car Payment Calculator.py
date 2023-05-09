#Sawera Ashfaq 
#Calculating A
#Request monthly payment P of car load PV with interest rate r
#for numbers of months n 
#formula= P=r*PV/(1-(1+r)**-n)
#with 2 digits after decimal breakpoint
PV=float(input('Enter principle amount :$'))
r=float(input('Enter annual interest rate :%'))
r=r/1200
n=float(input('Enter the term (number of years):'))
P=(r*PV)/(1-(1+r)**-n)
print('The monthly payment is $ %.2f'% P)