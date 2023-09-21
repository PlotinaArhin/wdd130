import math

# Get two numbers from the user.
num_items = int(input(" What is the number of manufactured items : ")) 
items_per_box = int(input(" Please input the number of items per box :"))

# Calculate the number of boxes.
num_boxes = num_items // items_per_box

# Check if the remaining items does not fix the complete boxes.
remaining_items = num_items % items_per_box

# If there are remaining items , we need an additional box
if remaining_items > 0 :
    num_boxes = +1

    # print the result for the code 
    print( f" The number of required boxes is: {num_boxes }")