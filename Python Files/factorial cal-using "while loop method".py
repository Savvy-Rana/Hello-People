#Sawera Ashfaq 
# 02/09/2023
#Find the factorial of a user integer number 
number=int(input("Enter an integer number to find it factorial value:"))
factorial=1
i=1
while i!=number+1:
    factorial=factorial*i
    i=i+1
print ("Factorial for the",number, "is", factorial)