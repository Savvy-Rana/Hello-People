#Sawera Ashfaq 
# 02/09/2023
# Find the maximum score of a set of exam scores
max=0
num=int(input("Enter the number of students:"))
i=1
while i!= num+1:
    print("Enter student #",i,"score:")
    score=int(input(""))
    if score >max:
        max=score
        maxID=i
    i=i+1
print("The student # ",maxID,"has the maximum score",max)