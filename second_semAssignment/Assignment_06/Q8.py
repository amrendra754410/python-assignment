# Write a Python program to implement the linear search algorithm to find a target value in a list.
# (a) If the target is found, return its index.
# (b) If not found, return −1

import timeit
def linerSearch(list,num):
    tic=timeit.default_timer()
    resut=False
    for i in range(len(list)):
        if list[i]==num:
            resut=True
        else:
            resut=False
    if True:
        print("Found")
    else:
        print("Not Found")
    toc=timeit.default_timer()
    print("Exceuction time: ",(toc-tic))

list=[1,2,3,4,2,5,6,7,8,9,9,9,9,9,9,10,11,12,20,10,50,50,50,90,90,90,90,10,13,14,15,16,17,18,19,20]
num=int(input("Enter the number to find: "))
linerSearch(list,num)