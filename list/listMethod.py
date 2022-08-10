# Adding by Index: Insert
# ==========================================
# The Python list method .insert() allows us to add an element to a specific index in a list.

# The .insert() method takes in two inputs:

# The index you want to insert into.
# The element you want to insert at the specified index.
# The .insert() method will handle shifting over elements and can be used with negative indices.

# To see it in action let’s imagine we have a list representing a line at a store:

# store_line = ["Karla", "Maxium", "Martim", "Isabella"]
# "Maxium" saved a spot for his friend "Vikor" and we need to adjust the list to add him into the line right behind "Maxium".

# For this example, we can assume that "Karla" is the front of the line and the rest of the elements are behind her.

# Here is how we would use the .insert() method to insert "Vikor" :

# store_line.insert(2, "Vikor")
# print(store_line) 
# Would output:

#  ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']
# Some important things to note:

# The order and number of the inputs is important. The .insert() method expects two inputs, the first being a numerical index, followed by any value as the second input.

# When we insert an element into a list, all elements from the specified index and up to the last index are shifted one index to the right. This does not apply to inserting an element to the very end of a list as it will simply add an additional index and no other elements will need to shift.
# ======================================================================================================================================================================================