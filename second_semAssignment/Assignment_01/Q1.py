# # At Delhi University, students enroll in different courses. Given two sets:
# Set A: Students enrolled in Mathematics = { ”Amit”, ”Bhavna”, ”Chirag”, ”Deepak”, ”Esha” }
# Set B: Students enrolled in Physics = { ”Chirag”, ”Deepak”, ”Farhan”, ”Geeta”, ”Harsh” }
# Write a Python program to:

SetA={ "Amit", "Bhavna", "Chirag", "Deepak", "Esha" }
SetB={"Chirag", "Deepak", "Farhan", "Geeta", "Harsh"}
# a) Find students enrolled in either Mathematics or Physics.
union_AandB=SetA.union(SetB)
print(union_AandB)
# b) Find students enrolled in both Mathematics and Physics .
intersection_AandB=SetA.intersection(SetB)
print(intersection_AandB)
# c) Find students enrolled in Mathematics but not in Physics .
Sub_AandB=SetA.difference(SetB)
print(Sub_AandB)
# d) Find students enrolled in Physics but not in Mathematics.
Sub_BandA=SetB.difference(SetA)
print(Sub_BandA)





