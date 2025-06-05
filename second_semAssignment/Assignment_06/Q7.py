# Write a program to identify the element that appears most frequently in a list. Measure the execution
# time of the program and discuss its time complexity

import timeit
list=[1,2,3,4,2,5,6,7,8,9,9,9,9,9,9,10,11,12,20,10,50,50,50,90,90,90,90,10,13,14,15,16,17,18,19,20]
tic=timeit.default_timer()
count=0
max_count=0
for i in  range (len(list)):
    count1=0
    for j in range(len(list)):
        if i!=j:
            if list[i]==list[j]:
                count1 +=1
    if count1>count:
        count=count1
        max_count=i
print(list[max_count])
toc=timeit.default_timer()
print("time: ",toc-tic)