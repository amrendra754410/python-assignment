# Write a Python program that prints a pattern using both numbers and stars. The pattern should alternate between numbers and stars in each row.
#   1 * 2 * 3 *
#   * 4 * 5 * 6
#   7 * 8 * 9 *
#   * 10 * 11 *


count=1
for i in range(0,4):
    for j in range(0,6):
        if j%2==0:
            print(count,end=" ")
            count +=1
        else:
            print("*",end=" ")
    print()
