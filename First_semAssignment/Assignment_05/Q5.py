# Write a Python program that prints an inverted triangle of stars, where the number of rows is
# taken an input from the user.

num=int(input("Enter the n: "))
for i in range(0,num):
    for j in range(num,i,-1):
        print("*",end=" ")
    
    print()