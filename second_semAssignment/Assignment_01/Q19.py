# A school surveyed students’ subject preferences. The three subjects were Mathematics, Science, and
# English. The survey found: 
# Students who like Mathematics: 30
# Students who like Science: 25
# Students who like English: 20
# Students who like both Mathematics and Science: 10
# Students who like both Science and English: 8
# Students who like both Mathematics and English: 7
# Students who like all three subjects: 5
# Write a Python program to draw a Venn Diagram representing this data

# 

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Survey data
math = 30
science = 25
english = 20
math_science = 10
science_english = 8
math_english = 7
all_three = 5

# Create the Venn diagram
venn = venn3(subsets=(math - math_science - math_english + all_three,
                  science - math_science - science_english + all_three,
                  math_science - all_three,
                  english - math_english - science_english + all_three,
                  math_english - all_three,
                  science_english - all_three,
                  all_three),
            set_labels=('Mathematics', 'Science', 'English'))

# Add title and display
plt.title("Students' Subject Preferences")
plt.show()



