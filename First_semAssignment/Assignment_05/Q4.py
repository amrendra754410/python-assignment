# print floyd's triangle

row=5
cont=1
for i in range(1,row+1):
    for j in range(0,i):
        print(cont,end=" ")
        cont +=1
    print()