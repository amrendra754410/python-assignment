# Write a Python program that find the elements present in the first list but not in the second one.

# num=int(input("Enter the length of list: "))
# list1=[]
# list2=[]
# for i in range (num):
#     list1.append(int(input("Enter the value of 1st list: ")))
# for i in range (num):
#     list2.append(int(input("Enter the value of 2nd list2: ")))

list1=[54,5,8,4,8,45,5]
list2=[5,5,5,8,54,9,9,6,100]

list3=[]
for i in list1:
    if i is not list2:
        list3.append(i)
print(list3)
