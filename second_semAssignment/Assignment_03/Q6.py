import pandas as pd

# Create the dataset as a dictionary
data = {
    "CustomerID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Country": ["USA", "USA", "USA", "Germany", "India", "India", "USA", "Canada", "India", "India"],
    "State": ["Georgia", "Georgia", "Florida", "Bavaria", "Karnataka", "Karnataka", "Florida", "Ontario", "Maharastra", "Maharastra"],
    "ZipCode": [30332, 30331, 30912, 80331, 560001, 569081, 30123, 43134, 578234, 578923]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Filter: Country = USA AND State = Georgia
filtered_df = df[(df["Country"] == "USA") & (df["State"] == "Georgia")]
print(filtered_df)




filtered_df1=df[(df["Country"]=="USA") | (df["State"]=="Ontario")]
print(filtered_df1)

filtered_df2=df[(df["Country"]!="USA")]
print(filtered_df2)



