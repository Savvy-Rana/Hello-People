n=[0,1,2,3,4,5,6,7,8]
print(n)
n.append(9)
print(n)
n=n+[10]
print(n)
print("Is number 77 in the list:")
print(77 in n)
print("Is number 2 in list")
print(2 in n)
del n[0]
print(n)
n.reverse()
print(n)
n.clear()
print(n)