from fractions import Fraction


def prob_of_events(sample_space,event):
    if event.issubset(sample_space)!=True:
        print("Event must subset of the sample space")
    else:
        return Fraction(len(event),len(sample_space))
    
    
s={1,2,3,4,5,6}
e={1,2}
print(prob_of_events(s,e))