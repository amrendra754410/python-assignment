#3. Find the Largest Number in 5 user defined numbers using for and while.
i=1
largest_number=0
while i<=5:
    number=int(input("Enter the number: "))
    if(number>largest_number):
        largest_number=number
    i+=1
print(f"largest number is {largest_number}")

