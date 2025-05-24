list1=[5,58,45,4,5,41,5,41]
list2=[56,5,9,4,5,5,4,8,2,5]
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)