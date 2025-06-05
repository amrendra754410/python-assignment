import timeit
import math

def isPrime(num, range1):
    tic = timeit.default_timer()
    is_prime = True;
    for i in range (2, range1):
        if (num%i==0):
            is_prime = False
    if (is_prime):
        print("Prime")
    else:
        print("Not Prime")
    toc = timeit.default_timer()
    print("Execution Time: ", (toc-tic))


num = int(input("Enter Number: "))
isPrime(num, num)
num_sqrt = int(math.sqrt(num)) + 1
isPrime(num, num_sqrt)