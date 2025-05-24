# At Tech University, students can enroll in various advanced courses based on the prerequisite coursesthey have completed. The university wants to determine a relation between prerequisite courses andadanced courses based on specific eligibility criteria.
# • Prerequisite Courses (Set A) = { ”Math-101”, ”Physics-101”, ”CS-101”, ”Statistics-101” }
# • Advanced Courses (Set B) = { ”Machine Learning”, ”Quantum Computing”, ”Data Science”,
# ”Computer Vision”, ”AI Ethics” }
# The eligibility criteria are as follows:
# c) Computer Vision requires CS-101 and Math-101.
# d) AI Ethics is open to all students who have completed any one prerequisite.
# Write a Python program to generate the complete relation R, representing which prerequisite course
# allows enrollment in which advanced course.

SetA={"Math-101", "Physics-101", "CS-101", "Statistics-101"}
SetB={ "Machine Learning", "Quantum Computing", "Data Science", "Computer Vision", "AI Ethics" }

resul1=[]
# a) Machine Learning and Data Science require Math-101 or Statistics-101.
for sub1 in SetB:
    if sub1 in {"Machine Learning" , "Quantum Computing"}:
        for sub2 in SetA:
            if sub2 in {"Math-101" , "Statistics-101"}:
                resul1.append((sub1, sub2))
print(resul1)

# b) Quantum Computing requires Math-101 and Physics-101.
for sub1 in SetB:
    if sub1=="Quantum Computing":
        for sub2 in SetA:
        