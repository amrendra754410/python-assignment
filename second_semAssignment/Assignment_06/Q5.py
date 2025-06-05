# Write a program to find the first duplicate element from a given list. Measure the execution time of
# the program and discuss its time complexity


import timeit
list=[1,2,3,4,2,5,6,7,8,9,10,11,12,10,13,14,15,16,17,18,19,20]
# num=int(input("Enter the number: "))
tic=timeit.default_timer()
found = False

for i in range(len(list)):
    for j in range(len(list)):
        if i!=j:
            if (list[i] == list[j]):
                print("Duplicate")
                print(list[i])
                found = True
                break
    if (found):
        break
                

toc=timeit.default_timer()
print("Execution Time: ",(toc-tic))



