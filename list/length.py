# Length
# Often, we’ll need to find the number of items in a list, usually called its length.

# We can do this using a built-in function called len().

# When we apply len() to a list, we get the number of elements in that list:

# my_list = [1, 2, 3, 4, 5]
 
# print(len(my_list))
# Would output:

# 5
# Let’s find the length of various lists!

# Instructions
# 1.
# Calculate the length of long_list and save it to the variable long_list_len.

# Checkpoint 2 Passed

# Stuck? Get a hint
# 2.
# Use print() to examine long_list_len.

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# We have provided a completed range() function for the variable big_range.

# Calculate its length using the function len() and save it to a variable called big_range_length.

# Note: Range objects do not need to be converted to lists in order to determine their length

# Checkpoint 4 Passed

# Stuck? Get a hint
# 4.
# Use print() to examine big_range_length.

# Checkpoint 5 Passed

# Stuck? Get a hint
# 5.
# Change the range() function that generates big_range so that it skips 100 instead of 10 steps between items.

# How does this change big_range_length?

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# Your code below: 
long_list_len = len(long_list)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)

# After change 
big_range = range(2, 3000, 100)
big_range_length = len(big_range)

print(big_range_length)