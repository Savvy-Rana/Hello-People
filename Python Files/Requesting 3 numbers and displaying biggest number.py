#request 3 integers then display the biggest number 

num1,num2,num3=eval(input("Enter 3 integers"))
int(num1), int(num2),int(num3)
if num1>num2 and num1>num3:
    print(num1, "is the biggest number")
elif num2>num1 and num2>num3:
    print(num2, "is the biggest number")
else:
    print(num3, "is the biggest number")