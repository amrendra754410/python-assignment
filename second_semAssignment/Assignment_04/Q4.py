from fractions import Fraction


red_ball=3
blue_ball=2
total_ball=red_ball+blue_ball

prob1_Red=Fraction(red_ball,total_ball)
# print(prob1_Red)


prob2_Red=Fraction(red_ball-1,total_ball-1)
# print(prob2_Red)

total_prob_2reball=prob1_Red*prob2_Red

print("Probability of drowing 2 red ball: ",total_prob_2reball)





