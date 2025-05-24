# At XYZ University, students have the opportunity to join various clubs based on their interests. The university has three prominent clubs: the Coding Club, which has 120 members; the Robotics Club,ith 95 members; and the AI Club, which consists of 80 students. However, some students are members of multiple clubs. Specifically, 30 students are part of both the Coding and Robotics Club,25 students are in both the Robotics and AI Club, and 20 students are enrolled in both the Codingand AI Club. Additionally, there are 10 students who are members of all three clubs. The university administration wants to determine the total number of unique students participating in at least one of these clubs by applying the Inclusion-Exclusion Principle.



# Club membership counts
coding = 120
robotics = 95
ai = 80

# Overlaps between clubs
coding_robotics = 30
robotics_ai = 25
coding_ai = 20

# Students in all three clubs
all_three = 10

# Applying the Inclusion-Exclusion Principle
total_unique = (
    coding + robotics + ai
    - (coding_robotics + robotics_ai + coding_ai)
    + all_three
)

print("Total number of unique students:", total_unique)


