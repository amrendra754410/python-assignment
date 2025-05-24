import random
from fractions import Fraction
dice=[1,2,3,4,5,6]
sum_7=0
for i in range (5000):
    roll1=random.choice(dice)
    roll2=random.choice(dice)
    if(roll1+roll2==7):
        sum_7 +=1
        

#probability of getting sumof 7
probability=Fraction(sum_7,5000)
print("Number of times getting sum 7: ",sum_7)
print("probability of getting sumof 7: ",probability)
    