# A school conducted a survey to find out how many students play Cricket and Football. The survey
# results are:
# Students who play Cricket: 40
# Students who play Football: 35
# Students who play both Cricket and Football: 15
# Write a Python program to draw a Venn Diagram representing this data.

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

cricket=40
football=35
both=15

venn2(subsets=(cricket-both,football-both,both),set_labels=('Cricket','Football'))

plt.title
plt.show()

