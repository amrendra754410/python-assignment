import time


print("Les's play a game.")
while True:
    colour=input("Choose a colour: red,gree, or yellow")
    if(colour.lower()=="green"):
        print("you must wait 5 second to learn your fate.")
        time.sleep(5)
        print("You win! Excellent choice!")
        break
    elif(colour.lower()=="yellow"):
        print("you must wait 2 second to learn your fate.")
        time.sleep(2)
        print("You lose! You must start over.")
    else:
        print("you must wait 4 second to learn your fate.")
        time.sleep(4)
        print("You lose! You must start over.")
