'''
Unit 2 Review
'''

'''
R ead
E valuate
P rint
L oop
'''

'''
while True: # infinite loop

    # ask the user to enter their name or to quit
    name = input('\nPlease enter your name or "done" to quit: ')

    # if the user entered 'done'
    if name == 'done':
        print('Goodbye')
        break # end the loop

    # main body of code goes here
    # ...
    # ...
    print(f'Thanks for playing, {name}!')
'''

'''
while True: # infinite loop
    print('Welcome to the program!')

    again = input("Do you want to play again? y/n: ")

    if again == 'n':
        print("Goodbye!")
        break
'''

'''
# Ask the user for a list of colors with no duplicates
colors = [] # blank list to hold colors
while True:
    # ask the user for a color
    color = input("Please enter a color or 'done' to quit: ")

    # if the user enters 'done', break the loop
    if color == 'done':
        print(f'You entered: {colors}')
        break

    # ensure the user enters a color that isn't in the list
    while color in colors:
        print(f'Color already in the list: {color}')
        color = input("Please enter a color: ")
    
    # once the user enters a color that isn't in the list
    # add it to the list
    print(f'Color added to the list: {color}')
    colors.append(color)
    print(colors)

    # exits at 5 colors
    if len(colors) == 5:
        print(colors)
        break

'''

'''
limit = input('How many numbers do you want to add to the list: ')
limit = int(limit)

numbers = []
for x in range(limit): # while len(numbers) < limit
    number = input('Please enter a number: ')

    # convert number to float
    number = float(number)

    numbers.append(number)
    print(f'{number} added to the list')

print(numbers)
'''

# ------------------------------------------------ #

# Functions

# absolute value is a numbers distance, positive or negative, from 0
def absolute_value(number):
    if number < 0:
        number *= -1

    return number

# print(absolute_value(-9))
# print(absolute_value(-123123))
# print(absolute_value(123123))

# ----------------------------------------------------- #

def add(a = 2, b = 2):
    '''
    DOCSTRING - short explanation of the function.
    
    Returns the sum of two numbers, 'a' and 'b'
    '''
    return a + b

# print(add(2, 9))
# print(add())         # a = 1, b = 0 (both defaults used)
# print(add(9, 2))     # a = 9, b = 2
# print(add(6))        # a = 6, b = default
# print(add(b=6))      # a = default, b = 6
# print(add(b=6, a=4)) # b = 6, a = 4

num1 = 6
num2 = 6
# print the return from a function within an f-string
# print(f'{num1} + {num2} = {add(num1, num2)}')

# -------------------------------------------------------- #


# *args (arguments) / **kwargs (keyword arguments)
# * - each arg is one piece of data
# ** - each kwarg is two pieces of data (variable_name = value)
def print_args_kwargs(*args, **kwargs):
    print(args)

    # loop through all arguments (args)
    for arg in args:
        print(arg)

    print(kwargs)

# print_args_kwargs(3.14, 'cat', True, word1 = 'fish', word2 = 'dog', word3='zebra')

# ----------------------------------------------------- #

# take in any number of numbers and add them together
def add_em_up(*nums):
    '''
    Return the sum of any arbitritrary number of numbers (*nums)
    '''
    total = 0 # starting total

    # loop through all numbers and add them to the total
    for num in nums:
        total += num

    return total

# print(add_em_up(34, 54, 99, 10, 14, 10, 5, 1919191, 213930493))

# ----------------------------------------------------- #

# SCOPE - 'bubbles' where variables exist
# all the way to the left is called the 'global scope'

# y is defined in the global scope
y = 99

# subtract() is also defined in the global scope
def subtract(a, b):
    # print(y)
    
    # y += 1 # UnboundLocalError because y isn't defined within the function

    x = 5 # x is defined in the scope of the function subtract()

    return a + b

# print(x) # x only exists inside subtract()
# print(subtract(1,2))