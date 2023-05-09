"""
Sawera Ashfaq
Python program using 2 functions to display the results
"""

def getscore():
     score=int(input("Enter your score [0-100]:"))
     return score
def getgrade(score):
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    elif score>50:
        grade="F"
    elif score>=0:
        grade="F"
    return grade 
s=getscore()
g=getgrade(s)
print ("Your score", s,"has a grade", g)