num=int(input("Enter the number: "))
num_str=str(num)
len_num=len(num_str)
print(len_num)
sum=0
for i in num_str:
    sum=sum+(int(i)**len_num)
if(sum==num):
    print(num,"is a amicable number")
else:
    print(num,"is not amicable number")
