# Write a python program to create two data frames and merge those two data frames on a common
# column.


import pandas as pd

# First DataFrame: Employee details
data1 = {
    "EmployeeID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
}
df1 = pd.DataFrame(data1)

# Second DataFrame: Employee salaries
data2 = {
    "EmployeeID": [1, 2, 3],
    "Salary": [50000, 60000, 55000]
}
df2 = pd.DataFrame(data2)

# Merge DataFrames on 'EmployeeID'
merged_df = pd.merge(df1, df2, on="EmployeeID")

# Display merged DataFrame
print(merged_df)
