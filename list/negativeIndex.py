# Accessing List Elements: Negative Index
# What if we want to select the last element of a list?

# We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.

# Consider the following list with 6 elements:

# pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]
# If we select the -1 index, we get the final element, "love".

# print(pancake_recipe[-1])
# Would output:

# love
# This is equivalent to selecting the element with index 5:

# print(pancake_recipe[5])
# Would output:

# love


# Instructions
# 1. Create a variable called last_element.
#  Assign the last element in shopping_list to the variable last_element using a negative index.
# 2.Now select the element with index 5 and save it to the variable index5_element. 
# 3.Use print to display both index5_element and last_element.Note that they are equal to "cereal"!

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element)
print(index5_element )
