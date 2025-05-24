# In a social media app, friendships are symmetric: If A is a friend of B, then B must also be a friend of A. Define a Python function to verify if a given friendship relation is symmetric and complete the
# missing pairs if necessary. Given two relations are:
# • R1 : {(”Anurag”, ”Nitish”), (”Priyabrata”, ”Koustav”), (”Prateek”, ”Asutosh”)}
# • R2 : {(”Priya”, ”Nikita”), (”Nikita”, ”Priya”), (”Sancheeta”, ”Shreyashree”),(”Shreyashree”,
# ”Sancheeta”)}


R1={("Anurag", "Nitish"), ("Priyabrata", "Koustav"), ("Prateek", "Asutosh")}
R2={("Priya", "Nikita"), ("Nikita", "Priya"), ("Sancheeta", "Shreyashree"),("Shreyashree","Sancheeta")}

def check_symm(Set1):
    check = True
    for (a,b) in Set1:
        if (b,a) not in Set1:
            print("Required Relations to be symmetric: ",b,a)
            check = False

    return check

print(check_symm(R1))
print(check_symm(R2))