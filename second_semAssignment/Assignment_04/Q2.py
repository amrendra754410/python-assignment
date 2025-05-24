import random
dice=[1,2,3,4,5,6]
six=0
for i in range(1000):
    roll=random.choice(dice)
    if(roll==6):
        six +=1

print("probabilty of 6: ",six)