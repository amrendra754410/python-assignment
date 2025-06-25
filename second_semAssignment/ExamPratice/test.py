import math
import scipy
import scipy.special
import time
import timeit

# print(math.factorial(20)/(math.factorial(4)*math.factorial(20-4)))
# print(scipy.special.binom(20,4))

number=1000
starttime=time.time()
tic=timeit.default_timer()
list=[]
time.sleep(1)
for i in range (number):
    list.append(i)

# endtime=time.time()
toc=timeit.default_timer()
print(time.time()-starttime)
print(toc-tic)