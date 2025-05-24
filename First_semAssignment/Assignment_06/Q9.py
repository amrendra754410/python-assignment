# Write a Python program that compute the sum of all elements in a tuple of tuples.                Example: ((1, 2),(3, 4), (5, 6)), sum = 21


tuple=((1,2),(3,4),(4,4),(5,6))
set1=set(tuple)
print(set1)
len=len(set1)
print(len)
sum=sum(sum(i)for i in tuple)
print(sum)

