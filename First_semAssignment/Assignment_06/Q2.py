# Write a Python program that check if one set is a subset or superset of another..

empty_set=set()
empty_set.add(1)
empty_set.add(2)
empty_set.add(3)    #1,2,3
set1=empty_set
set2={5,10,2,2,2,1,3}
print(set1.issubset(set2))
print(set1.issubset(set1))
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set1.issuperset(set1))
print(set2.issuperset(set1))
