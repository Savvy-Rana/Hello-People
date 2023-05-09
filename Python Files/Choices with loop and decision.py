#Sawera Ashfaq
#02/13/23
#choices:loop and decision
choice =0
while choice<1 or choice>5:
    print("Welcome to your choice of simple calculators!")
    print("Below are the 4 simple math calculations you can doing using 2 numbers:")
    print ("1- Addition: a + b")
    print ("2- Subtraction: a - b")
    print("3- Multiplication: a*b")
    print ("4- Division :a/b")
    print ("5-Exit")
    choice=int(input("Enter your choice [1-5]:"))
while choice>=1 and choice<=5:
    if choice ==5:
        print ("Good Bye") 
        break
    a=int(input("Enter the 1st number a: "))
    b=int(input("Enter the 2nd number b: "))
    if choice==1:
        result=a+b
        print ("=============================")
        print(a, "+",b, "=",result )    
        print ("=============================")
    elif choice==2:
        result=a-b
        print ("=============================")
        print(a, "-",b,"=", result )
        print ("=============================")
    elif choice==3:
        result=a*b
        print ("=============================")
        print(a,"*", b, "=", result )
        print ("=============================")
    elif choice==4:
        while b==0:
            print("b can not be 0")
            b=int(input("Enter 2nd number b:"))
        result=a/b
        print ("=============================")
        print(a,"/",b,"=", "%.2f" %result)
        print ("=============================")
    print ("Lets do this again:")
    print ("Please pick your option:")
    print ("1- Addition: a + b")
    print ("2- Subtraction: a - b")
    print("3- Multiplication: a*b")
    print ("4- Division :a/b")
    print ("5-Exit")
    choice=int(input("Enter your choice [1-5]:"))
    