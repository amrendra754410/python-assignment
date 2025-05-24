# Create a program that asks the user for the total purchase amount and applies a discount:
#    • Over 1000: 10% discount
#    • Between 500 and 1000: 5% discount
#    • Below 500: No discount

purchase_amount=int(input("Enter the Total purchage amount: "))
discount=0
if(purchase_amount>1000):
    print(purchase_amount-(purchase_amount*(10/100)))
elif(purchase_amount>500 and purchase_amount<=1000):
    print(purchase_amount-(purchase_amount*(5/100)))
else:
    print("No Discount")
