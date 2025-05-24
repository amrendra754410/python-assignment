# At City Library, books are categorized based on genre and age group. The library wants to establish
# a relation that maps which genres are recommended for which age groups.
# • Genres (Set A) = { ”Fiction”, ”Non-Fiction”, ”Mystery”, ”Science”, ”Fantasy” }
# • AgeGroup (Set B) = { ”Children”, ”Teen”, ”Adult” }
# The relation R follows these constraints:
# Write a Python program to generate and print the valid (Genre, AgeGroup) pairs forming the relation R.

SetA={"Fiction", "Non-Fiction", "Mystery", "Science", "Fantasy"}
SetB={"Children", "Teen", "Adult"}
# i. Children can read Fiction and Fantasy.

relation = []


for genre in SetA:
    if genre == "Fiction" or genre == "Fantasy":
        relation.append((genre, "Children"))

# ii. Teens can read all genres except Non-Fiction.
for genre in SetA:
    if genre != "Non-Fiction":
        relation.append((genre, "Teen"))

# iii. Adults can read all genres.

for genre in SetA: 
    relation.append((genre, "Teen"))

print(relation)