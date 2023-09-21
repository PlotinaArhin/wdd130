import math 

# Get two numbers from the user.
num_items = int(input(f"Enter the number of manufactured boxes: "))
items_per_boxes = int(input("Enter the number of items per boxes: "))

# Compute the number of boxes by dividing 
# and then calling the math.ceil functions.
num_boxes = math.ceil(num_items/items_per_boxes)

# Display a blank line.
print()

# Display the result to the user to see.
print(f" for the {num_items} items ,  packing  {items_per_boxes}"f"items in each boxes , you will need {num_boxes} boxes.")