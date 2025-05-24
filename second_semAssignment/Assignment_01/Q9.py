# A professor teaches exactly one subject. Given a set of professor-subject assignments, check if it forms a function.
# • professor&subject = {(”Dr. Smith”, ”Math”), (”Dr. Johnson”, ”Physics”), (”Dr. Smith”, ”Physics”)}

professor_subject={("Dr. Smith", "Math"), ("Dr. Johnson", "Physics"), ("Dr. Smith", "Math")}

def is_function(relation):
    seen = {}
    for professor, subject in relation:
        if professor in seen and seen[professor] != subject:
            return False
        seen[professor] = subject
        print(seen)
    return True

professor_subject = {
    ("Dr. Smith", "Math"),
    ("Dr. Johnson", "Physics"),
    ("Dr. Smith", "Math")
}

print("Is function?", is_function(professor_subject))