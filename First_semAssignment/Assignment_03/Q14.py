# Write a Python program that takes a word as input and categorizes the word based on length:
#   • Words with length less than 4 are ”Short”
#   • Words with length between 4 and 7 are ”Medium”
#   • Words with length greater than 7 are ”Long”

user=input("Enter the word: ")
if(len(user)<4):
    print(f"Word is Short ({user})")
elif(len(user)>7):
    print(f"Word is Long ({user})")
else:
    print(f"Word is Mdium ({user})")