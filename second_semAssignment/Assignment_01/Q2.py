# A tech company maintains records of employees with expertise in Python and Java. The HR team
# wants to analyze skill distribution using in-built set functions. Given the following sets:
# Set A (Employees skilled in Python) = { ”Amit”, ”Bhavna”, ”Chirag”, ”Deepak”, ”Esha”, ”Farhan” }
# Set B (Employees skilled in Java) = { ”Chirag”, ”Deepak”, ”Farhan”, ”Gaurav”, ”Harsh” }
# Write a Python program to perform the following operations using in-built set functions:



SetA={"Deepak" "Amit", "Bhavna", "Chirag", "Esha" }
SetB={"Chirag", "Deepak", "Farhan", "Geeta", "Harsh"}
# a) Find whether ”Deepak” is skilled in Python.
if "Deepak" in SetA:
    print("yes")
# b) Check if all Python-skilled employees are also skilled in Java.

def check_all_skilled(SetA, SetB):
    for p1 in SetA:
        if p1 not in SetB:
            return False
    return True

print(check_all_skilled(SetA, SetB))


