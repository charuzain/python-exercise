List Methods
As we start exploring lists further in the next exercises, we will encounter the concept of a method.

In Python, for any specific data-type ( strings, booleans, lists, etc. ) there is built-in functionality that we can use to create, manipulate, and even delete our data. We call this built-in functionality a method.

For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go between the parenthesis of the method ( ).

An example of a popular list method is .append(), which allows us to add an element to the end of a list.

append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')
 
print(append_example)
Will output:

['This', 'is', 'an', 'example', 'list']

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
# print(example_list)

#Using Remove
example_list.remove(5)
# print(example_list)

Growing a List: Append
We can add a single element to a list using the .append() Python method.

Suppose we have an empty list called garden:

garden = []
We can add the element "Tomatoes" by using the .append() method:

garden.append("Tomatoes")
 
print(garden)
Will output:

['Tomatoes']
We see that garden now contains "Tomatoes"!

When we use .append() on a list that already has elements, our new element is added to the end of the list:

# Create a list
garden = ["Tomatoes", "Grapes", "Cauliflower"]
 
# Append a new element
garden.append("Green Beans")
print(garden)
Will output:

['Tomatoes', 'Grapes', 'Cauliflower', 'Green Beans']
Let’s use the .append() method to manipulate a list.



Growing a List: Plus (+)
When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).

Below, we have a list of items sold at a bakery called items_sold:

items_sold = ["cake", "cookie", "bread"]
Suppose the bakery wants to start selling "biscuit" and "tart":

items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)

Would output:

['cake', 'cookie', 'bread', 'biscuit', 'tart']
In this example, we created a new variable, items_sold_new, which contained both the original items sold, and the new items. We can inspect the original items_sold and see that it did not change:

print(items_sold)
Would output:

['cake', 'cookie', 'bread']
We can only use + with other lists. If we type in this code:

my_list = [1, 2, 3]
my_list + 4
we will get the following error:

TypeError: can only concatenate list (not "int") to list
If we want to add a single element using +, we have to put it into a list with brackets ([]):

my_list + [4]
========================================

NTRODUCTION TO LISTS
Accessing List Elements
We are interviewing candidates for a job. We will call each candidate in order, represented by a Python list:

calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]
First, we’ll call "Juan", then "Zofia", etc.

In Python, we call the location of an element in a list its index.

Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.

Here are the index numbers for the list calls:

Element	Index
"Juan"	0
"Zofia"	1
"Amare"	2
"Ezio"	3
"Ananya"	4

In this example, the element with index 2 is "Amare".

We can select a single element from a list by using square brackets ([]) and the index of the list item. If we wanted to select the third element from the list, we’d use calls[2]:

print(calls[2])
Will output:

Amare
Note: When accessing elements of a list, you must use an int as the index. If you use a float, you will get an error. This can be especially tricky when using division. For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated to the float 2.0.

To solve this problem, you can force the result of your division to be an int by using the int() function. int() takes a number and cuts off the decimal point. For example, int(5.9) and int(5.0) will both become 5. Therefore, calls[int(4/2)] will result in the same value as calls[2], whereas calls[4/2] will result in an error.

========================================
Shrinking a List: Remove
We can remove elements in a list using the .remove() Python method.

Suppose we have a filled list called shopping_line that represents a line at a grocery store:

shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]
We could remove "Chris" by using the .remove() method:

shopping_line.remove("Chris")
 
print(shopping_line)
If we examine shopping_line, we can see that it now doesn’t contain "Chris":

["Cole", "Kip", "Sylvana"]
We can also use .remove() on a list that has duplicate elements.

Only the first instance of the matching element is removed:

# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Remove a element
shopping_line.remove("Chris")
print(shopping_line)
Will output:

["Cole", "Kip", "Sylvana", "Chris"]
Let’s practice using the .remove() method to remove elements from a list.

========================================
