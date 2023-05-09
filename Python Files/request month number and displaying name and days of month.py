#sawera Ashfaq
#2/1/2023 
# month number [1-12] then decide and display  
#The month name and number of days 
num = int(input('Enter month number [1-12]: ')) 
if num==1: 
    month="January" 
    days=31 
elif num==2: 
    month="February" 
    days=28 
elif num==3: 
    month="March" 
    days=31 
elif num==4: 
    month="April" 
    days=30 
elif num==5: 
    month="May" 
    days=31 
elif num==6: 
    month="June" 
    days=30 
elif num==7: 
    month="July" 
    days=31 
elif num==8: 
    month="August" 
    days=31 
elif num==9: 
    month="September" 
    days=30 
elif num==10: 
    month="October" 
    days=31 
elif num==11: 
    month="November" 
    days=30 
elif num==12: 
    month="December" 
    days=31 
print("The month number", num, "is",month," and has " ,days, "days") 