# In a company, an employee can have a supervisor. If A supervises B, then B cannot supervise A (antisymmetric relation). Given a list of supervision relations, check if the relation is anti-symmetric.
# • supervision = {(”Alice”, ”Bob”), (”Alice”, ”Charlie”), (”Bob”, ”David”)}



supervision = {("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David")}

def is_anti_symmetric(R):
    for (a, b) in R:
        if a != b and (b, a) in R:
            return False
    return True

print(is_anti_symmetric(supervision))