

# Sawera Ashfaq
# Nested List  

P=100
Alow=[P*(1+2.5/100)**n for n in range(11)]
Ahigh=[P*(1+5.0/100)**n for n in range(11)]
amounts=[Alow,Ahigh]  # 2 lists
print(amounts)   
print(amounts[0])    # first list from the "amounts" list which is Alow.
print(amounts[1])     # second list fromt he "amounts" list which is Ahigh
