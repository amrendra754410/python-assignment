size_choice=input("Is this a personal or family pizza(Type 1 for personal,Type 2 for family)")
if(size_choice=="1"):
    size_choice="personal"
else:
    size_choice="family"


source_choice=input("Which sauce would you like? (Marimara->M,Garlic->G)")
if(source_choice.upper()=="M"):
    sauce="Marimara"
else:
    sauce="Garlic Cream"


cheese_choice=input("Would you like cheese on your pizza? (Yes->Y,No->N)")
if(cheese_choice.upper()=="Y"):
    cheese_choice2=input("Would you like regular chesse or extra chesse? (Regular->R,Extra->E)")
    if(cheese_choice2.upper()=="R"):
        cheese="Regular"
    else:
        cheese="Extra"
    troppings=input("Would you like mushrooms on your pizza? (Yes->Y,No->N)")
    if(troppings.upper()=="Y"):
        tropping="Mushrooms"
    else:
        tropping="No Mushrooms"
else:
    cheese="No cheese"
    troppings=input("Would you like mushrooms on your pizza? (Yes->Y,No->N)")
    if(troppings.upper()=="Y"):
        troppings="Mushrooms"
    else:
        tropping="No Mushrooms"
print(f"You want a {size_choice} pizza with {sauce} sauce, {cheese} and {troppings}")


    
