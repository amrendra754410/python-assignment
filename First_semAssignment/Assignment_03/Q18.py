# Create a number guessing game where the program generates a random number between 1 and 100.
# The user must guess the number, and the program gives hints like ”Too high” or ”Too low” until the
# correct number is guessed.
import random
print("Welcome to guessing game")
print("I have select a number between 0 to 100 can you gusse which number am guse.")
random=random.randint(0,100)
attempt=0
while(True):
    user=int(input("Enter the number:"))
    attempt+=1
    if(random>user):
        print("Too High")
    elif(random<user):
        print("Too Low")
    else:
        print(f"congratulations you gusse a number {attempt} attempt.")
    break
