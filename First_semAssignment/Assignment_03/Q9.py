item=int(input("Enter the item: "))
box_capacity=int(input("Enter the item box: "))
full_box=item/box_capacity
leftOver_item=item%box_capacity
print(f"Full box={full_box} leftOver item={leftOver_item}")
