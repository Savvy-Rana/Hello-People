#Sawera Ashfaq 
#Calculating A
#Request Principle, interest rate and term to calculate the final amount
#formula=A=P*(1+)r/100))**n
#with 2 digits after decimal breakpoint
P=float(input('Enter principle amount :$'))
r=float(input('Enter annual interest rate :%'))
n=float(input('Enter the term (number of years):'))
A=P*(1+(r/100))**n
print('the final amount is $ %.2f'% A)