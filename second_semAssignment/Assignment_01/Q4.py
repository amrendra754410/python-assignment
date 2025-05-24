# ITER is conducting course registration for the new semester. Each student can enroll in any of the
# available subjects. Given a list of students and a list of subjects, generate all possible student-subject
# enrollment pairs.
# • Students: Asutosh, Ayushman, Mohit, Priya
# • Subjects: Mathematics, Physics, Computer Science, Economics

# student={"Asutosh","Ayushman","Mohit","Priya"}
# subject={"Mathematics","Physics","Computer Science","Economics"}

students = {"Asutosh", "Ayushman", "Mohit", "Priya"}
subjects = {"Mathematics", "Physics", "Computer Science", "Economics"}

# Generate all possible enrollment pairs
for student in students:
    for subject in subjects:
        print(f"{student} : {subject}")
