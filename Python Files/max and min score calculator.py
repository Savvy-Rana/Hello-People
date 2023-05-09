#Sawera Ashfaq
#Assignment # 2 - Q1
# Python program to ask for a set of scores and then determining the
# lowest and the highest scores.
max=0
min=100
print("Lets calculate the highest and the lowest exam score!")
num=int(input("1-Please enter the total # of students:"))
i=1
while i!=num+1:
    print ("Enter student#", i, "score:")
    score=int(input(""))
    if score>max:
        max=score
        maxID=i
    elif score<min:
        min=score
        minID=i
    i=i+1
print("The student #", maxID, "has the highest score of",max)
print("===================================================")
print("The student #", minID, "has the lowest score of", min)
    