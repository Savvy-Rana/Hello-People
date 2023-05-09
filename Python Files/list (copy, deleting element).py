a=[1,2,3,4,5]
b=a.copy()     #copy the list a as b and whenever you make any changes to b, a will not be affected. 
b[3]=0
print(a)
print(b)
