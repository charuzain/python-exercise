# Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system.

# Write a space.py program that helps Codey keep track of their target weight by:

# Checks which number planet is equal to.
# It should then compute their weight on the destination planet.
# Here is the table of conversions:

# #	Planet	Relative Gravity
# 1	Venus	   0.91
# 2	Mars	   0.38
# 3	Jupiter	 2.34
# 4	Saturn	 1.06
# 5	Uranus	 0.92
# 6	Neptune	 1.19

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1 :
  weight = weight * 0.91
elif planet == 2 :
  weight = weight * 0.38
elif planet == 3 :
  weight = weight * 2.34
elif planet == 4 :
  weight = weight * 1.06
elif planet == 5 :
  weight = weight * 0.92
if planet == 6 :
  weight = weight * 1.19

print("Target Weight is :" , weight)