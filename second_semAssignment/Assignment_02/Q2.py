# Write a Python program to generate the truth table for the following Boolean function:
# F(A, B, C) = (A ∨ B) ∧ (¬C)

from sympy import symbols
from sympy.logic.boolalg import Or, And,Not
from sympy.logic.boolalg import truth_table

A,B,C=symbols('A B C')

F=And(Or(A,B),Not(C))

tt=truth_table(F,[A,B,C])

print("A B C | F(A,B,C)")
print("-----------------")

for row in tt:
    inputs, output = row
    print(f"{int(inputs[0])} {int(inputs[1])} {int(inputs[2])} | {int(output)}")

