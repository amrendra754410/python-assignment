#13. Write a python program that determines loan eligibility based on the following conditions:
#    • If income is greater than 50,000 and credit score is above 700, they are eligible.
#    • If income is between 30,000 and 50,000, they are eligible only if: Their credit score is above
#    750 or they have been employed for more than 5 years.
#    • If income is less than 30,000, they are not eligible.

income=int(input("Enter your income: "))
creditScore=int(input("Enter the number: "))
working_Exp=int(input("Worling Experiance(year):"))
if(income>50000 and creditScore>700):
    print("Your are eligible for loan")
elif(income<50000 and income>30000 ):
    if(creditScore>750 and working_Exp>5):
        print("Your are eligible for loan")
else:
    print("Your are not eligible for loan")
