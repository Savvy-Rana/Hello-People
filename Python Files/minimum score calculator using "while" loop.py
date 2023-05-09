#Sawera Ashfaq 
# 02/09/2023
# Find the minium score of a set of exam scores
min=100
num=int(input("Enter the number of students:"))
i=1
while i!= num+1:
    print("Enter student #",i,"score:")
    score=int(input(""))
    if score<min:
        min=score
        minID=i
    i=i+1
print("The student # ",minID,"has the minimum score of",min)