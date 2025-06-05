def sequential_flow():
    print("Sequential Flow:")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sum_ab = a + b
    print("The sum is:", sum_ab)

def selection_flow():
    print("Selection Flow:")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

def repetitive_flow():
    print("Repetitive Flow:")
    n = int(input("Enter how many numbers you want to print: "))
    count = 1
    while count <= n:
        print(count, end=' ')
        count += 1
    print()  # for newline


print("1. Sequential")
print("Choose a flow control type:")
print("2. Selection")
print("3. Repetitive")
    
choice = input("Enter 1, 2 or 3: ")

if choice == '1':
    sequential_flow()
elif choice == '2':
    selection_flow()
elif choice == '3':
    repetitive_flow()
else:
    print("Invalid choice. Please enter 1, 2, or 3.")


