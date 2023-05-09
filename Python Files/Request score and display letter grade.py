#sawera Ashfaq
#2/1/2023 
#Request user score then decide and display the score and the grade 
score = int(input("Enter your score [0-100]: ")) 
if score>=90: 
    grade='A' 
elif score>=80: 
    grade='B' 
elif score>=70: 
    grade='C' 
elif score>=60: 
    grade='D' 
elif score>=0: 
    grade='F' 
print("Your score is",score," and your grade is",grade) 