
import timeit
list=[1,2,3,4,2,5,6,7,8,9,10,11,12,20,10,50,50,50,90,90,10,13,14,15,16,17,18,19,20]
# num=int(input("Enter the number: "))
tic=timeit.default_timer()
l=[]
for i in range(len(list)):
    for j in range(len(list)):
        if i!=j:
            if (list[i] == list[j] and list[i] not in l):
                l.append(list[i])
                print("Duplicate")
                print(list[i])
                found = True
                break
    
                

toc=timeit.default_timer()
print("Execution Time: ",(toc-tic))



