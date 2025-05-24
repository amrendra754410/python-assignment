#Write a Python program that takes a number as input from the user and checks whether it is a perfect
#square. Display an appropriate message based on the result.
import math

def check_perfectsquare(num):
    root=int(math.sqrt(num))
    if root*root==num:
        return True
    else:
        return False
    

user=int(input("Enter the number: "))
print(check_perfectsquare(user))