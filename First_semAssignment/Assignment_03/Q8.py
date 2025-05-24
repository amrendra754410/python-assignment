age=int(input("Enter the age: "))
if(age>0 and age<=3):
    print("Your age toddler.")
elif(age>=13 and age<=19 ):
    print("Your age teenager.")
elif(age>19 and age<60):
    print("Your age adults.")
elif(age>=60):
    print("Your age senior citizen")