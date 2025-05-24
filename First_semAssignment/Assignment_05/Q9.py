# Write a Python program that checks for Armstrong numbers in a given range from 1 to n. An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the numberof digits.

input=int(input("Enter the number: "))
str_input=str(input)
digit=len(str(input))
sum=0
for i in str_input:
    sum +=int(i)**digit
if(sum==input):
    print(f"{input} is armstrong number.")
else:
    print(f"{input} is not armstrong number.")

