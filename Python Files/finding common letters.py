#Sawera Ashfaq 
# 02/09/2023
# Ask the user for 2 words and then search for the common letters
print("Lets find the common letters in between 2 words!")
word1=input("Enter Word #1:")
word2=input("Enter Words #2:")
common=""
for letter in word1:
  if(letter in word2)and (letter not in common):
    common=common+letter
if common=="":
        print ("The words have no characters in common.")
else:
    print("The words have the following letter in common",common)
