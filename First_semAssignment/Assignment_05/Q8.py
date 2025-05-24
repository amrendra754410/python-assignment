# Write a Python program that prints a multiplication table in reverse order. The user should input the value of n for which the table needs to be printed.

num=int(input("Enter the number(n): "))
for i in range(10,1,-1):
    print(f"{num}X{i}={num*i}")