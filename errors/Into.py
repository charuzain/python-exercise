# In Python, there are many different ways of classifying errors, but here are some common ones:

# SyntaxError: Error caused by not following the proper structure (syntax) of the language.
# NameError: Errors reported when the interpreter detects a variable that is unknown.
# TypeError: Errors thrown when an operation is applied to an object of an inappropriate type.

# Syntax Errors
# ==================
# When we are writing Python programs, the interpreter is our first line of defense against errors.

# SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.

# Here’s an example of a SyntaxError error message:

# File "script.py", line 1
#   print(Hello world!)
#                   ^
# SyntaxError: invalid syntax
# The interpreter will tell us where (the file name and line number) it got into trouble and its best guess as to what is wrong.
# After reading the error message, we can assume that the cause for this error is a lack of quotation marks around Hello world!.

# Some common syntax errors are:

# # Misspelling a Python keyword.
# # Missing colon :.
# # Missing closing parenthesis ), square bracket ], or curly brace }.


 # Name Errors
# ===============================
# # A NameError is reported by the Python interpreter when it detects a variable that is unknown.

# # This can occur if a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined. The Python interpreter will display the line of code where the NameError was detected and indicate which name is found that was not defined.

# # Here’s an example of a NameError error message:

# # File "script.py", line 1, in <module>
# #     print(score)
# # NameError: name 'score' is not defined
# # This error is suggesting that the variable score was never defined in the program. Oops.

# # Some common name errors are:

# # Misspelling a variable name.
# # Forgetting to define a variable.


# Type Errors
# ===============================

# A TypeError is reported by the Python interpreter when an operation is applied to a variable of an inappropriate type.

# This can occur in Python when one attempts to use an operator on something of the incorrect type.

# For example, let’s see what happens when we try and add together two incompatible types:

# piggy_bank = '2' + 0.25
# There will be an TypeError error message:

# Traceback (most recent call last):
#   File "script.py", line 1, in <module>
#     piggy_bank = '2' + 0.25
# TypeError: must be str, not float
# This error is reporting that 0.25 is not a string.

# Some common type errors are:

# Accidentally adding or subtracting a string value.
# Call a function on something of the incorrect type.


# There is also another type of error that doesn’t have error messages that we will cover down the line:

# Logic errors: Errors found by the programmer when the program isn’t doing what it is intending to do.