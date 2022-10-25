"""
Programming 102
101 Review
"""

"""
Units 1 & 2 - variables, strings & string operations, f-strings, input(), int/float
"""

# = is the assignment operator. Assigns the value on the right to the variable on the left.
# define a variable 'animal' and assign the string 'dog' to it using =

# ------------------------------------------------------------------------------------- #

# a "function" is a named code block that performs a specific task
# functions are executed by placing parentheses () after their name
# data can be passed into the function by placing it within the parentheses
# functions will always return a value as well


# type(object) - return the datatype of the object


# string (str) - sequence of textual characters surrounded by quotes
# --------------------------------------------------------------------------------------- #

# change the value within the variable 'animal' to 'cat'

# --------------------------------------------------------------------------------------- #

# concatenation - adding strings together to form a single string

# add the string 'fish' to the value within the variable 'animal'
# redefined 'animal' with the result

# --------------------------------------------------------------------------------------- #

# a 'method' is a function that manipulates only the object to which it belongs
# an object's methods are accessed using a dot after the object's name

# .upper() - return an uppercase version of the string

# .replace(old, new) - return a copy of the string with the old replaced with the new within it

# methods can be chained. Each one operates on the return value of the previous

# ---------------------------------------------------------------------------------------------- #

"""
Escape Characters

- Denoted with a backslash \ before the character 
- "Escape" the normal rules of strings to allow the characters to behave differently than normal
"""

# print("hello "world"") # Error! Quotes cancel each other

# Solution 1 - printing quotes with mismatched sets:
# print("hello "world"")

# Solution 2 - printing quotes with escape characters
# print("hello "world"")

# formatting string with escape characters
# print("ABC") # \n - new line character
# print("ABC") # \t - horizontal

# ------------------------------------------------------------------------------------------- #

'''
Python Variable Names

- must start with a letter or underscore
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9 and _)
- are case sensitive (age, Age, AGE are 3 different variables)
'''

# python_variable_and_function_names_use_snake_case
# all lowercase words, separated with underscores

# ThisIsPascalOrTitleCase - used for defining classes in Python
# ALLCAPS - generally used for constant variables

# for Python styling conventions check out PEP8 (Python Style Guide)

# ----------------------------------------------------------------------------------------- #

# f-strings
# 'f' stands for 'formatted'. f-strings allow Python expressions to be formatted into strings

# note: concatenation only works with strings
# other datatypes will need to be "typecast" using str() before concatenation

# f-strings don't care about datatype


# ----------------------------------------------------------------------------------------- #
'''
user_string = input(prompt_message)

Print the prompt message and wait for the user to hit enter.
Once the user hits enter, anything they typed in the terminal will be returned.
Return value can be saved in a variable such as 'user_string'
'''

# ------------------------------------------------------------------------------------------ #
'''
# input() always returns a string

# typecast to a number
# int(object) - return the object as an integer, if possible
# float(object) - return the object as a float, if possible

# convert the number string to float

'''
# ----------------------------------------------------------------------------------------- #

# integer (int) - whole numbers
# float (float) - decimal numbers

# arithmetic operators

# addition +
# subtraction -

# multiplication *
# exponentiation ** (x^y)

# 'regular' division / (results in a float)
# 'floor' division // (rounds down to the nearest integer)

# modulus % (remainder after division)

# ----------------------------------------------------------------------------------- #

# ReAssignment Operators

x = 4

# ReAssignment Operators - combine the arithmetic and assignment operators

# ReAssignment operators exist for each arithmetic operators
x += 2 # x = x + 2
x -= 2 # x = x - 2
x *= 2 # x = x * 2
x **= 2 # x = x ** 2
x /= 2 # x = x / 2
x //= 2 # x = x // 2
x %= 2 # x = x % 2


# ----------------------------------------------------------------------------------------- #

'''
Unit 3 - booleans, comparisons, logical statements, conditionals
'''

# datatype - boolean
# True / False

# booleans in Python are Capitalized

# -------------------------------------------------------------------------------------- #

# THIS CAN BE SKIPPED, IF NEEDED

# typecast to boolean
# bool(object) - return a boolean representation of the object

# Truthy/Falsey
# if an object has value, it will convert to True
# if an object has no value, it will convert to False
'''
# Falsey values
''    # blank string has no value
[]    # blank list has no value
0     # number 0 has no value
None  # None has no value
etc...
'''

# -------------------------------------------------------------------------------------- #

# Comparison Operators - compare two pieces of data and result in a boolean

# All comparisons need two sides



# == check equality - True
# != check inequality - False

# < 'strictly' less than - False
# <= less than or equal to - True

# > 'strictly' greater than - False
# >= greater than or equal to - True

# ---------------------------------------------------------------------------------------- #

# Logical Operators - combine comparisons and result in a single boolean
# and, or, not

# logical statements need two comparisons


# and - True only if BOTH comparisons are True
# True - both comparisons are True
# False - left comparison (x == 2) is False

# or - True if at least ONE comparison is True
# True - right comparison (x < 10) is True
# False - both comparisons are False

# not - flip a boolean

# 'not' is often used with the keyword 'in' to check if an item is in a sequence

# ---------------------------------------------------------------------------------------- #

'''
Conditional Statements
----------------------
Run different code blocks based on the outcome of comparisons
Keywords: if, elif, else

Code Block:
A section of code that executes together.
In Python, code blocks are defined using horizontal indentation

---------------------------------------------------------------------------------------

Conditional Rules:
------------------

- must start with if
- all ifs will be checked
- elif are only checked if the preceding if and other elifs were False
- else is triggered if all other conditions were False
- if/elif will only be checked until a True condition is found

---------------------------------------------------------------------------------------

Conditional Statements Will Always Have:
------------------------------------------
- 1 if
- 0 -> infinity elifs
- 0 or 1 else

'''

# ------------------------------------------------------------------------------------------- #

'''
Unit 4 - lists / for loops
------

Datatype: list

Lists are 'ordered' and 'changeable' sequences of items.
Lists are created using square brackets []
List items are separated with commas ,
'''

# define a list of colors

# organized vertically

# ------------------------------------------------------------------------------------------- #

# list items can be retrieved using their positions in the list
# an item's position in the list is called its 'index'

# place the index of the item in square brackets
# after the list's variable name to retrieve the item
# list indices always start at 0


# can't use non-existent indices

# In Python, negative indices are allowed
# -1 will always be the last index

# # can't use non-existent indices

# ------------------------------------------------------------------------------------ #

# strings are ordered sequences as well

# strings are NOT 'changeable'

# lists ARE changable

# ------------------------------------------------------------------------------------- #

# cannot add values this way

# items can be added using list methods

# .append(item) - add a single item to the end of the list

# .insert(index, item) - add the item at the index

# .extend(sequence) - add the items from the sequence to the end of the list

# -------------------------------------------------------------------------------------- #

# items can be removed with list methods as well

# .remove(item) - remove the first occurrence of the item from the list

# .pop(index) - remove the item at the index and return it. index defaults to -1 if not provided

# ------------------------------------------------------------------------------------------- #

# .sort() - sort a list in ascending order (returns None)

# .sort() returns None

# ---------------------------------------------------------------------------------------------- #


# loop - a code block that repeats until a certain condition is met

# for item in sequence - loop through each item in the sequence

# for/in - Python operators
# item - arbitrary variable name to store each item as the loop visits it
# sequence - string, list or other 'iterable' (loopable) object

# ---------------------------------------------------------------------------------------------- # 
# for x in range() - loop a certiain number of times

# range(stop) - return a range of numbers from 0 to stop-1

# range(start, stop, step)

# -------------------------------------------------------------------------------------- #

# while loop

'''
while some_condition == True:
    # loop this
    # code block
'''

# -------------------------------------------------------------------------------------- #

# loop controls
# continue, break, else
