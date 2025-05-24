import random
compnumber=random.randint(0,100)
for i in range(5,0,-1):
    usernumber=int(input(f"Choose a number between 1 and 100. You have {i} guesses: "))
    if(compnumber==usernumber):
        print("You win!")
        exit()
    elif(compnumber>usernumber):
        print("Your number is too small!")
    elif(compnumber<usernumber):
        print("You number is too large!")

print(f"The rand no was {compnumber}")