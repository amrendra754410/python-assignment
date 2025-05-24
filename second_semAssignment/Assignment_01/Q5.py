# A board game uses two dice. Find all possible outcomes of rolling the dice.

setA={1,2,3,4,5,6}
for dice1 in setA:
    for dice2 in setA:
        print(f"dice1:{ dice1} | dice2: {dice2}")