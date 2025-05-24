import random
head=0
tail=0
for i in range(1000):
    toss=random.choice(['H','T'])
    if toss=='H':
        head = head+1
    else:
        tail = tail+1
    
print("Head: ",head)
print("Tail: ",tail)