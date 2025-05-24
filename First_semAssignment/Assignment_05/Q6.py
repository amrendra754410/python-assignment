# Write a Python program that uses nested loops to count how many times each character 
# appears in a given string.


arr = []
input = input("Enter a string: ")
for i in input:
    count = 0
    if i not in arr:
        for j in input:
            if (j==i):
                count += 1
        arr.append(i)
        
        print(f"{i} occurs {count} times.")
print(arr)