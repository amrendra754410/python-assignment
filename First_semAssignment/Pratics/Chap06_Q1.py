# import random
# randomNumber=random.randint(0,10)
# newNumber=randomNumber*3
# print(newNumber)
# print("Yes")


# number = input("Enter the number between 1 and 10.")
# print(10/int(number))
# while(True):
#     print("hello")

online_store={
    "keychain": 0.75,
    "tshirt": 8.50,
    "bottle": 10.00
    }
print(online_store)

# HOw many items buying
choicekey = int(input("Enter the number of keychains: "))
choicetshirt = int(input("Enter the number of tshirts: "))
choicebottle = int(input("Enter the number of bottle: "))

if (choicekey > 9):
    online_store["keychain"]=0.65
if (choicebottle>9):
    online_store["bottle"]=8.75
if (choicetshirt > 9):
    online_store["tshirt"]=8.00

perkey = input("Will you personalize keychain (yes/no): ")
pertshirt = input("Will you personalize tshirt (yes/no): ")
perbottle = input("Will you personalize bottle (yes/no): ")


if perkey.lower() == "yes":
    online_store["keychain"] += 1 
if pertshirt.lower() == "yes":
    online_store["tshirt"] += 5
if perbottle.lower() == "yes":
    online_store["bottle"] += 7.5


keychainprice = choicekey*online_store['keychain']
tshirtprice = choicetshirt*online_store['tshirt']
bottleprice = choicebottle*online_store["bottle"]

print(f"Price of {choicekey} keychains is ${keychainprice}")
print(f"Price of {choicetshirt} tshirts is ${tshirtprice}")
print(f"Price of {choicebottle} bottles is ${bottleprice}")
total = keychainprice+tshirtprice+bottleprice
print(f"TOtal: {total}")
