# 1) We have decided to get into the grocery store business. Our manager Calla has decided to store all the inventory purchases in a list to help track what products need to be ordered.

# Let’s create a list called order_list with the following values (in this particular order):

# "Celery", "Orange Juice", "Orange", "Flatbread"

# Print order_list to see the current list.

# 2. We are in luck! We actually found a spare case of "Flatbread" in our back storage. We won’t need to order it anymore. Let’s remove it from order_list using the .remove() method.

# Print order_list to see the current list.

# 3. Our store has grown to be a huge success! We decided to open a second store and require a new order list. Calla has done us the favor of putting one together.

# Create a new list called new_store_order_list and assign it the following values (in order):

# "Orange", "Apple", "Mango", "Broccoli", "Mango"

# Note: Our second store is going to need two orders of mangos so the value is duplicated.

# Print new_store_order_list to see the current list.

# 4. We are in luck again! We actually found a spare case of "Mango" in our back storage.

# We won’t be needing to place two orders anymore.

# Let’s remove it from new_store_order_list using the .remove() method.

# Print new_store_order_list to see the current list.

# 5. Calla ran to tell us some important news! She asked us to remove "Onions" from our new new_store_order_list. If we double-check our list, we will notice we don’t have "Onions" on our list.

# Let’s see what happens when we try to remove an item that does not exist.

# Call the .remove() method with the value of "Onions" on our new_store_order_list list.

# When we call .remove() on a list with a value that does not exist, we will receive a ValueError.

# Traceback (most recent call last):
#   File "script.py", line 18, in <module>
#     new_store_order_list.remove("Onions")
# ValueError: list.remove(x): x not in list



# Your code below: 

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list )

new_store_order_list.remove('Mango')
print(new_store_order_list )

new_store_order_list.remove('Onion')