list1=[1,2,3,2,8]
#list2=[1,"abc","abc",1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("NOT palindrome")