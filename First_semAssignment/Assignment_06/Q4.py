# Write a Python program that remove all duplicate elements of a list.


num=int(input("Enter the length of list: "))
arr=[]
for i in range(num):
    arr.append(int(input("Enter the value of list: ")))

noduplicatearr = []
for i in arr:
    if i not in noduplicatearr:
        noduplicatearr.append(i)
print(noduplicatearr)