#Sawera Ashfaq 
# 02/09/2023
#FGuessing a number game with Set number
import random 
max=25
n=25
playername=input("Enter your name to play a game:")
print ("Welcome to guessing a number game",playername,)
print(" Guess a number between 1 and", max)
guess=0
while guess!=n:
    guess=int(input("Your try:"))
    if guess<n:
        print ("Too low")
    if guess >n:
        print ("Too High")
print ("Congratulation,you won!, The correct number is",n,".")