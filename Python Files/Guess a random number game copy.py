#Sawera Ashfaq 
# 02/09/2023
#FGuessing a number game with Set number
import random 
max=25
n=random.randint(1,max)
playername=input("Enter your name to play a game:")
print ("Welcome to guessing a number game",playername,)
print(" Guess a number between 1 and", max)
guess=0
while guess!=n:
    guess=int(input("Try:"))
    if guess<n:
        print ("Too Low")
    if guess >n:
        print ("Too High")
print ("Congratulation",playername,"you won!, The correct number is",n,".")