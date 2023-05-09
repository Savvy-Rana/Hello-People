#Sawera Ashfaq 
#2/1/2023 
#Request user score [0-100] then: 
#display "Pass" if the score is between 70 and 100  
#display "Fail" if the score 0 to 69 
#display "Your score is not between 0-100" 
score = int(input("Enter your score [0-100]: ")) 
if score>=70 and score<=100: 
    print("You Pass") 
elif score>=0 and score<=69: 
    print("You Fail") 
else: 
    print("Your score is not between 0 and100") 