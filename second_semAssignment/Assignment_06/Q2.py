# Write a program that counts how many even and odd numbers are in a list. Measure the execution
# time of the program and discuss its time complexity

import time
import timeit
tic=timeit.default_timer()
count_even=0
count_odd=0
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in list:
    if i%2==0:
        count_even +=1
    else:
        count_odd +=1
print("Even count: ",count_even)
print("Odd count: ",count_odd)
# time.sleep(1)
toc=timeit.default_timer()
print("execution time: ",(toc-tic))


