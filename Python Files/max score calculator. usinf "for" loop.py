#Sawera Ashfaq 
# 02/09/2023
# Find the maximum score of a set of exam scores
max=0
num=int(input("Enter the number of students:"))
for i in range (1, num+1):
    print("Enter student #",i,"score:")
    score=int(input(""))
    if score >max:
        max=score
        maxID=i
print("The student # ",maxID,"has the maximum score",max)