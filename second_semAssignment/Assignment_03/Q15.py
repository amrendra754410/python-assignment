# Write a python program using scipy for a problem where in a lottery, you must select 6 numbers from
# a total of 49. You want to know how many different combinations of 6 numbers can be chosen from
# 49.


from scipy.special import comb

# Total number of numbers to choose from
n = 49

# Number of selections
k = 6

# Calculate number of combinations
combinations = comb(n, k)

print(f"The number of different combinations of 6 numbers from 49 is: {combinations}")
