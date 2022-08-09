# In script.py, your coworker Carolyn wrote a Fortune Cookie program that is supposed to print out a possible fortune based on a random number and an if/elif/else statement.
# Oh no, there are three SyntaxError errors inside script.py!
# Can you find them all?

# Fortune Cookie Program 🥠

# import random

# fortune = random.randint(0, 4)

# if fortune == 0
#   print("May you one day be carbon neutral")
# elif fortune == 1:  
#   print("You have rice in your teeth")
# eli fortune == 2:
#   print("No snowflake feels responsible for an avalanche")
# elif fortune == 3:
#   print("You can only connect the dots looking backwards"
# elif fortune == 4:
#   print("The fortune you seek is in another cookie")

# SOLUTION
# Fortune Cookie Program 🥠

import random

fortune = random.randint(0, 4)
print(fortune)

if fortune == 0:
  print("May you one day be carbon neutral")
elif fortune == 1:  
  print("You have rice in your teeth")
elif fortune == 2:
  print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
  print("You can only connect the dots looking backwards")
elif fortune == 4:
  print("The fortune you seek is in another cookie")