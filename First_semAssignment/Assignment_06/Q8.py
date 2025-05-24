# Write a function to merge two tuples into a single tuple without duplicates.

tuple=(5,8,5,4,9,5,48)
tuple1=(5,8,4,5,9,8,58)
set1=set(tuple)
set2=set(tuple1)
set3=set1.intersection(set2)
print(set3)