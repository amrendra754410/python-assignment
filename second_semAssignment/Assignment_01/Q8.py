# In a family tree, every person is related to themselves (reflexive relation). Given a parent-child relation, check if it includes reflexivity.
# • people = {”Alice”, ”Bob”, ”Charlie”}
# • parent&child = {(”Alice”, ”Bob”), (”Bob”, ”Charlie”)}

people={"Alice", "Bob", "Charlie"}
parent_child = {("Alice","Bob"), ("Bob", "Charlie")}

def check_ref(Set1,Set2):
    for p1 in Set1:
        if (p1,p1) not in Set2:
            return False
    return True

print(check_ref(people,parent_child))