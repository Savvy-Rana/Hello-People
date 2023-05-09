#Sawera Ashfaq 
# 02/09/2023
#Find the factorial of a user integer number 
import random 
max=25
n=random.randint(1,max)
print ("Welcome to the guessing a number game:")
print(" Guess a number between 1 and", max)
guess=0
while guess!=n:
    guess=int(input("Your try:"))
    if guess<n:
        print ("Too low")
    if guess >n:
        print ("Too High")
print ("Congratulation,you won!, The correct number is",n,)