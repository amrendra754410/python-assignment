import timeit
tic=timeit.default_timer()
power=int(input("Enter tye number: "))
for i in range (100**power+1):
    print(i)

toc=timeit.default_timer()
print("toc time: ",toc)
final_time=toc-tic
print("Final time: ",final_time)