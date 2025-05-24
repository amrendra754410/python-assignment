#12. Write a python program to check eligibility based on age and height.
age=int(input("Enter the number: "))
height=int(input("Enter the height(cm): "))
if(age>=18 and height>=153):
    print("You are eligibile.")
else:
    print("Your are not eligibile.")