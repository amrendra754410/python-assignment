# A flight network records direct flights between cities. If there is a flight from A to B and from B to C,
# then there should be a direct or indirect flight from A to C (transitive relation). Check if the relation
# is transitive.
# • flights = {("New York", "London"), ("London", "Paris"), ("Paris", "Berlin"), ("New York","Paris")}

flights = {("New York", "London"), ("London", "Paris"), ("New York","Paris")}
def check_tran(Set1):
    for(a,b) in Set1:
        for(x,c) in Set1:
            if (x==b):
                if(a,c) not in Set1:
                    return False
    return True

print(check_tran(flights))


