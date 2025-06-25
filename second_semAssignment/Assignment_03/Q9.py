# Write a python program to create a data frame of an office with 60 employees and sort the data frame
# by one or more columns.



import pandas as pd

# Create simple employee data
data = {
    "EmployeeID":[1,2,3,4,5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 45000, 55000, 60000, 47000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by Department and Salary
sorted_df = df.sort_values(by=["Department", "Salary"])

# Display sorted DataFrame
print(sorted_df)
