# 1. Use square brackets ([ and ]) to select the 4th employee from the list employees. Save it to the variable employee_four.

# 2. Paste the following code into script.py:
# print(employees[8])
# What happens? Why?
# Selecting an element that does not exist produces an IndexError.

# 3. In the line of code that you pasted, change 8 to an index that exists so that you don’t get an IndexError.

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four = employees[3]
# print(employees[8]) -> IndexError.

print(employees[6])