#6. Print a diamond-shaped pattern using stars (*), where the number of rows is n. The top half should be
#   a pyramid, and the bottom half should be an inverted pyramid.

n=int(input("Enter the n: "))
for i in range(n):
    space = " "*(n-i)
    star = "*"*(2*i-1)
    print(space+star)
for i in range(n,0,-1):
    space = " "*(n-i)
    star = "*"*(2*i-1)
    print(space+star)
