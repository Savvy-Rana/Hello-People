# Sawera Ashfaq 
# Functions

def amount(n):
    P=100           # P is a local value to this loop!
    r=5.0           # <--- this r is local value to this loop
    return P*(1+r/100)**n           # r that is being used here is local 
A=amount(int(input("Enter the number of years:")))      #this code for user input
# A=amount(5)       # this code for set number of years
print("$%.2f" %A)