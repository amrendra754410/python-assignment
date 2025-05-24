# Write a Python program that create two sets and perform the following operations: union,     intersection,difference, and symmetric difference.

empty_set=set()
empty_set.add(1)
empty_set.add(2)
empty_set.add(3)    #1,2,3
set1=empty_set
set2={5,10,2,2,2,1,}
print(set2.union(set1))
print(set1.union(set2))
print(' ')
print(set1.intersection(set2))
print(" ")
print(set1.difference(set2))
print(" ")
print(set1.symmetric_difference(set2))



