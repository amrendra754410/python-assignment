# 1. Verify whether the following two logical expressions are equivalent using Python and the sympy
#    library:
#    P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)
#    Hint: Use the function simplify logic from the sympy library.


from sympy import symbols
from sympy.logic.boolalg import Or, And, simplify_logic

# Define symbols
P, Q, R = symbols('P Q R')

# Define the two expressions
expr1 = And(P, Or(Q, R))           # P ∧ (Q ∨ R)
expr2 = Or(And(P, Q), And(P, R))   # (P ∧ Q) ∨ (P ∧ R)

# Simplify both expressions
simplified_expr1 = simplify_logic(expr1)
simplified_expr2 = simplify_logic(expr2)

# Check equivalence
equivalence = simplified_expr1 == simplified_expr2

# Output
print("Simplified Expression 1:", simplified_expr1)
print("Simplified Expression 2:", simplified_expr2)
print("Are the expressions equivalent?", equivalence)
