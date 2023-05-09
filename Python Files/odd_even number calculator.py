#Sawera Ashfaq 
# 02/09/2023
# Ask the user for an integer than print odd and even numbers all the way to that number 
num=int(input("Enter an integer number:"))
print("odd numbers:")
for x in range (1, num, 2):
    print (x)
print("Even numbers:")
for x in range (2, num,2):
    print(x)