import timeit
tic=timeit.default_timer()
print("tic time: ",tic)
a=[1,2,3,4,5,6,7,8,9]
number=int(input("Enter the number: "))
for i in range(len(a)):
    if a[i]==number:
        print("Yes")
    else:
        print("No")

toc=timeit.default_timer()
print("toc time: ",toc)
final_time=toc-tic
print("Final time: ",final_time)