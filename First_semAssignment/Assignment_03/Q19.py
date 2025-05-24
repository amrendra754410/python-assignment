# Write a program that calculates the Body Mass Index (BMI) given a person’s weight (in kg) and
# height (in meters) and classifies the result according to these ranges:
#   • BMI < 18.5: Underweight
#   • 18.5 ≤ BMI < 24.9 : Normal weight
#   • 25 ≤ BMI < 29.9: Overweight
#   • BMI ≥ 30: Obesity
#   Hint: Formula: BMI = weight/(height)**2

import math
body_mass=float(input("Enter the mass of body(in kg): "))
body_height=float(input("Enter the height of body(in m): "))
bmi=body_mass/(math.pow(body_height,2))
if(bmi<18.5):
    print(f"Your are underweight,your BMI is {bmi}")
elif(bmi>=18.5 and bmi<24.9):
    print(f"Your are overweight,your BMI is {bmi}")
else:
    print(f"Your are obesity,your BMI is {bmi}")
