# A group of students were surveyed about their knowledge of Hindi and English. The survey found:
# Students who know Hindi: 50
# Students who know English: 40
# Students who know both Hindi and English: 20
# Write a Python program to draw a Venn Diagram representing this data.


import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define the data
hindi = 50
english = 40
both = 20

# Create the Venn diagram
venn2(subsets=(hindi - both, english - both, both), set_labels=('Hindi', 'English'))

# Add title and display
plt.title("Students' Knowledge of Hindi and English")
plt.show()
