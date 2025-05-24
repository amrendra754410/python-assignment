# Write a python program that creates a data frame from a dictionary of lists and demonstrates basic
# operations like displaying data, getting column information, and accessing specific rows.
# greater than 85.
# • Write a python program to handle missing data in a DataFrame by filling missing values or
# dropping rows/columns that contain NaN.



import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [92, 85, 78, 90],
    "Subject": ["Math", "Science", "English", "Math"]
}
df = pd.DataFrame(data)


# • Write a python program to filter rows in a DataFrame based on students with an average mark
# Filter students with marks > 85
high_achievers = df[df["Marks"] > 85]
print("\nStudents with marks > 85:\n", high_achievers)


# Create a DataFrame with missing values
data_with_nan = {
    "Name": ["Alice", "Bob", "Charlie", None],
    "Marks": [92, None, 78, 90]
}
df_nan = pd.DataFrame(data_with_nan)

# Fill missing values
filled_df = df_nan.fillna("Unknown")
print("\nData after filling missing values:\n", filled_df)

# OR drop rows with missing values
dropped_df = df_nan.dropna()
print("\nData after dropping rows with missing values:\n", dropped_df)
