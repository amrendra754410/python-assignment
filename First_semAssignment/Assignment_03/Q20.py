# Write a program that takes a number (1–7) as input and prints the corresponding day of the week (1
#   = Sunday, 2 = Monday, etc.). If the input is not within 1–7, print Invalid day.

num=int(input("Enter the number(1-7): "))
match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    


