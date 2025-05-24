#   Write a Python program that takes three integers representing a day, month, and year. The program
#   should check if this date is valid considering:
#   • The day is valid for the given month and year (accounting for leap years).
#   • The month should be between 1 and 12.
#   • The day should be within the possible days of that month.
#   If valid, return ”Valid Date”, otherwise ”Invalid Date”.

day=int(input("Enter the Day: "))
month=int(input("Enter the month: "))
year=int(input("Enter the year: "))
if(day>=1 and day<=30 and month>=1 and month<=12):
    print(f"Enter day({day}) and month({month}) is Valid Date")
else:
    print(f"Enter day({day}) and month({month}) is In valid Date")