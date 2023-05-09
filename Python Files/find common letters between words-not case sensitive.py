#Sawera Ashfaq 
# 02/09/2023
# Ask the user for 2 words and then search for the common letters, *program is not case sensitive
print("Lets find the common letters in between 2 words!")
word1=input("Enter Word #1:")
w1=word1.lower()
word2=input("Enter Words #2:")
w2=word2.lower()
common=""
for letter in w1:
  if(letter in w2)and (letter not in common):
    common=common+letter
if common=="":
        print ("The words have no characters in common.")
else:
    print("The words have the following letter in common",common)
