# Write a Python program that remove all duplicate elements of a list

list=[5,28,5,6,94,5,5,94]
dub_list=[]


for i in list:
    if i not in dub_list:
        dub_list.append(i)
print(dub_list)