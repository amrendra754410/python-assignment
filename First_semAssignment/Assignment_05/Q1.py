# Create a simple text-based game where the player can choose actions 
# (e.g., ”move forward,” ”turn left,” ”quit”). 
# Use a break statement to exit the loop when the player chooses ”quit.”

def game():
    
    while True:
        print("Wellcome to game")
        user=input("Enter the comment: ")
        if user.lower()=="move forward":
            print("You are moving forward")
        elif user.lower()=="turn left":
            print("You are turning left")
        elif user.lower()=="quit":
            print("Goodbye!")
            break
        else:
            print("Invalid user. Please try again.")
    



game()
    

    