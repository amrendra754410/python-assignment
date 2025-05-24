# Using the same data given in (Q2), find the following:
#A tech company maintains records of employees with expertise in Python and Java. The HR team
# wants to analyze skill distribution using in-built set functions. Given the following sets:
# Set A (Employees skilled in Python) = { ”Amit”, ”Bhavna”, ”Chirag”, ”Deepak”, ”Esha”, ”Farhan” }
# Set B (Employees skilled in Java) = { ”Chirag”, ”Deepak”, ”Farhan”, ”Gaurav”, ”Harsh” }
# Write a Python program to perform the following operations using in-built set functions:


SetA={"Deepak","Amit", "Bhavna", "Chirag", "Esha" }
SetB={"Chirag", "Deepak", "Farhan", "Geeta", "Harsh"}
# a) Check if at least one employee has both skills
def at_least_check(Set1,Set2):
    for e1 in SetA:
        if e1 is not SetB:
            return True
    return False
print(at_least_check(SetA,SetB))

# b) Find employees skilled in either Python or Java, but not both.
intersecton=SetA.intersection(SetB)
union=SetA.union(SetB)
result = union - intersecton
print("Find employees skilled in either Python or Java, but not both.")
print(result)
# c) Make a copy of the Python-skilled employee set.
copy=SetA.copy()
print("Make a copy of the Python-skilled employee set.")
print(copy)
# d) Clear the Java-skilled employee set
clear=SetB.clear()
print("Clear the Java-skilled employee set")
print(clear)



