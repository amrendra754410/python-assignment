# Write a Python program that takes an integer n and prints the sum of even and odd numbers separately from 1 to n.
input=int(input("Enter the num: "))
count_even=0
count_odd=0
for i in range(0,input+1):
    if(i%2==0):
        count_even +=i
    else:
        count_odd +=i
print("Sum of even ",count_even)
print("sum of odd ", count_odd)