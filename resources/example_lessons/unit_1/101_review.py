'''
Programming 101 Review
'''

'''
Unit 1
'''

# Welcome to Programming 102

# single line comment

# print('Hello world') # say hello to the world

'''
Multi-line
comment
with single quotes
'''

"""
Multi-line
comment
with double quotes
"""

# print() # built in function in Python for displaying data in the terminal

# print('hello') # hello

# print multiple items
# print('pi:', 3.1415) # pi: 3.1415

# ------------------------------------------- #

# strings - textual data. Sequences of characters surrounded by quotes

'' # blank string
"" # blank string
# print(type('')) # <class 'str'> - print the datatype of '' using type()

'cat'
"dog"
"%^&*(&^^&8987678987789ib9b9  9 9 97 78"

'''
# print a multiline string
print("""
Welcome to
    PDX Code Guild
Programming 102
""")
'''

# ------------------------------------------- #

# Concatenation - adding strings together

# print('hello' + ' ' + 'world') # hello world (the space in between is in its own string)

# -------------------------------------------- #

# Datatype methods
# A method is a function (executed with parentheses) that
# manipulates the piece to which it is attached with a dot '.'

# print('abcdefg'.upper()) # ABCDEFG

# print('hello'.replace('h', 'j')) # jello

# methods can be chained. Each subsequent method operates on the result of the previous
# print('hello'.replace('e', 'i').replace('l', 'p').upper()) # HIPPO

# OOPS! Forgot the parentheses on the method call
# print('hello'.upper) # <built-in method upper of str object at 0x000001C450583E30>

# ------------------------------------------------ #

# Escape characters

# allow characters to be placed within a string that would normally break the code
# allow strings to be formatted

# escape characters are denoted with a backslash \

# print("Hello "world"") # Quotes cancel each other
# print('Hello "world"') # print double quotes within single
# print("Hello \"world\"")

# same as double quotes but with singles
# print('I don\'t like spam!')
# print("I don't like spam!")

# print('hello\nworld') # \n - newline

# print('hello\tworld') # \t - horizontal tab

# ----------------------------------------------------- #

'''
Unit 2
'''

# Variables
# are named storage spaces for data
# store any datatype
# become the datatype they store
# data within a variable can change

# store the string 'blue' in a variable called 'color'
color = 'blue' # = is the assignment operator
# print(color) # blue

# change the value within the variable color
color = 'green'
# print(color) # green

# string methods can be called on 'color', since it contains a string
# print(color.capitalize()) # Green

# concatenation with a string variable
# print('My favorite color is ' + color)


# Variable names
# Must start with a letter or underscore character
# cannot start with a numbers
# can only contain alpa-numeric characters and underscores
# are case sensitive (age, Age, AGE are THREE DIFFERENT variables)

# this_is_snake_case # *** variable naming convention in Python ***
# thisIsCamelCase
# ThisIsTitleOrPascalCase

city = 'Portland'
year_moved = 2010
current_year = 2020

# cannot concatenate other datatypes into a string
# any other datatypes need to be converted to string first with str()'
# print('Someone who moved to ' + city + ' in ' + str(year_moved) + ' will have lived there for ' + str(current_year - year_moved) + ' years in ' + str(current_year))

# f-strings - 'f' stands for 'formatted' because we're formatting other datatypes into a string
# f-strings allow Python expressions (bits of code) to be placed within a string with curly brackets {}

# print(f'Someone who moved to {city} in {year_moved} will have lived there for {current_year - year_moved} years in {current_year}')

# ------------------------------------------------------------------- #

'''
# input(prompt_message) - print the prompt and wait for the user to hit enter, returning their input string
color = input('Enter a color: ')
print(f"I like the color {color}.")
'''

'''
# input() ALWAYS returns a string
number = input("Enter a number: ")

# convert to a number with float() or int()
number = float(number)

print(number, type(number)) # 5.0 <class 'float'>
'''

# --------------------------------------------------- #

'''
Unit 3
'''

x = 17
y = 6

# Arithmetic operators
# print(x + y) # addition
# print(x - y) # subtraction
# print(x * y) # multiplication
# print(x / y) # regular division (returns a float)
# print(x // y) # floor division (always round down)
# print(x ** y) # exponentiation x^y
# print(x % y) # modulus remainder after division

# ------------------------------------------------ #

# print(x) # 17
x + 2 # doesn't change x
# print(x) # 17

# print(x + 2) # 19 - uses the current value of x but doesn't change it
# print(x) # 17

x = x + 2 # uses the current value of x, adds 2 and saves the result over the previous value
# print(x) # 19

# Re-Assignment Operators
x += 2 # x = x + 2
x -= 2 # x = x - 2
x *= 2 # x = x * 2
x /= 2 # # x = x / 2
x //= 2 # x = x // 2
x **= 2 # x = x ** 2
x %= 2 # # x = x % 2

# ----------------------------------------- #

# Datatype: Boolean
# True / False

a = True
b = False

# print(a, type(a)) # True <class 'bool'>
# print(b, type(b)) # False <class 'bool'>

# Truthy/Falsey - bool()

# pieces of data that have value are considered True
# pieces of data with no value are considered False

x = 0 # False
y = 1 # True

x = '' # False - blank string
y = 'a' # True - has at least one character

x = [] # False - blank list
y = [1, 2, 3] # True - has at least one item

# print(bool(x), bool(y))
# ---------------------------------------- #

# Comparisons - compare the values of two or more pieces of data
x = 5
y = 5

# print(x == y) # True - equality
# print(x != y) # False - inequality
# print(x < y) # False - less than
# print(x <= y) # True - less than or equal to
# print(x > y) # False - greater than
# print(x >= y) # True - greater than or equal to

# ------------------------------------------- #

# Logical operators - and / or / not
x = 5
y = 5

# and - return True only if BOTH sides are True
# print(x == y and x == 5) # True
# print(x == y and x == 10) # False

# or - return True if AT LEAST ONE side is True
# print(x == y or x == 10) # True
# print(x != y or x == 10) # False

# not - return the OPPOSITE boolean
# print(x == y) # True
# print(not x == y) # 

# ---------------------------------------------- #

# Conditional statements - if / elif / else

# Run different blocks of code based on which condition is True

x = 10
y = 10

# must start with if
if x < y:
    # if statement's 'code block' begins here
    output = 'x is less than 10'
elif x == 14:
    output = 'x is 14'
elif x > y: # elif will only be checked if the previous if or elifs are False
    output = 'x is greater than 10'
else:
    # else is triggered if no other condition was True
    output = 'x equals y. None of the other conditions were True.'


# print(output)

'''
Unit 4
'''

# datatype - lists

# lists are ordered and changeable sequences of items, 
# separated by commas and surrounded by square brackets []

numbers = [11, 22, 33] # list of integers
colors = ['red', 'green', 'blue'] # list of strings

# list items can be formatted vertically too
colors = [
    'red',
    'green',
    'blue'
]

# list items can be ANY datatype, including other lists
jumble = ['cat', 6, 3.145, True, None, [1, 2, 3]]

# list items can be referenced based on their position in the list
# a item's position in the list is called its index
# print(colors[0]) # red - list indices always start at 0
# print(colors[1]) # green
# print(colors[2]) # blue
# print(colors[3]) # IndexError: list index out of range

# index of a lists last item is the length of the list minus 1

# print(colors[-1]) # blue - index -1 is always the last item of the list
# print(colors[-2]) # green
# print(colors[-3]) # red
# print(colors[-4]) # IndexError: list index out of range

# change the value at index 1
colors[1] = 'yellow' 
# print(colors) # ['red', 'yellow', 'blue']

# index must exist to assign a value
# colors[40] = 'purple' # IndexError: list assignment index out of range

# adding items to a list

# .append(item) add the item to the end of the list
colors.append('purple')
# print(colors) # ['red', 'yellow', 'blue', 'purple']

# .insert(index, item) add the item at the index
colors.insert(1, 'teal')
# print(colors) # ['red', 'teal', 'yellow', 'blue', 'purple']

# remove items from the list

# .remove(item) remove the first occurrence of the item from the list
colors.remove('yellow')
# print(colors) # ['red', 'teal', 'blue', 'purple']

# .pop(index) remove the item at the index
colors.pop(0)
# print(colors) # ['teal', 'blue', 'purple']

# .sort() sort a list in ascending order (only works with numbers and strings)
colors.sort()
# print(colors) # ['blue', 'purple', 'teal']

colors.reverse() # flip a lists order
# print(colors) # ['teal', 'purple', 'blue']

# ----------------------------------------- #

import random

# print a random color from the list
# print(random.choice(colors))

# ---------------------------------------- #

# loops - code blocks that repeat based on a certain condition

# for loop

# for item in sequence
for color in colors:
    output = f'color: {color}'
    # print(output)

# ------------------------------ #

# print different things based on the color value
for color in colors:
    if color == 'blue':
        output = f'Ew, {color}'
    else:
        output = f'I like the color {color}'


    # print(output)

# --------------------------------# 

# using indicies with strings
# string at index 3
# print('abcdefg'[3]) # d

for letter in 'abcdefg':
    output = f'letter: {letter}'
    # print(output)

# ------------------------------- #


# for x in range() - loop a certain number of times

# range() is a built in function in python which generates a range of numbers
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(stop) - 0 through stop-1 
for x in range(10):
    output = f'x: {x}'
    # print(output)

# len(sequence) returns the length of the sequence
number_of_colors = len(colors)
# print(number_of_colors)

# loop over the indices of a list
for index in range(number_of_colors):
    color = colors[index] # grab the color at the current index

    # print(f'{index}: {color}')


# --------------------------------------------- # 

# while loop

counter = 0 
while counter < 10: # loop while this is True
    # print(counter)

    counter += 2

# ------------------------ #

# generate a list of 10 random numbers between 1 and
numbers = []
while len(numbers) < 10: # loop while less than 10 items in a list
    # generate a random integer between 1 and 100
    number = random.randint(1, 100)

    # add the numer to the list
    numbers.append(number)

# print(numbers)

# ----------------------------- #

# loop controls
# continue / break
'''
for x in range(10):

    if x == 3 or x == 6:
        print('...')
        continue # go to the top of the loop

    if x == 8:
        print('goodbye')
        break # end the loop

    print(x)
'''

# ----------------------------------------- #

# else with loops
'''
import string

# loop through the alphabet
for letter in string.ascii_lowercase:
    print(letter)

    # if letter == 'q':
    #     break # end the loop 'unnaturally'

else:
    # run this when a loop completes naturally
    print('end of alphabet')

'''