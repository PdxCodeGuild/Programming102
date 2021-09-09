'''
Programming 102
Unit 2 Review
'''

import random

'''
R ead
E valuate
P rint
L oop
'''

# -------------------------------------------------------------------------------- #

# This REPL will only loop if the user enters exactly 'yes'
'''
again = 'yes'

while again == 'yes':
    print("\nWelcome to the game!")

    # other code ...

    # ask the user if they want to play again
    again = input('Do you want to play again? yes/no: ')
'''
# ------------------------------------------------------------------------------- #
'''
# This REPL displays different things for 'y','n' and invalid options
# but will loop unless the user enters 'n'
while True: # infinite loop
    print("\nWelcome to the game!")

    # other code ...

    # ask the user if they want to play again
    again = input('Do you want to play again? y/n: ')

    # check the user's input
    if again == 'y':
        print("\nOkay! Let's play again!")

    elif again == 'n':
        print("\nGoodbye!")
        break # end the loop

    else:
        print("\nInvalid selection!")
'''
# ------------------------------------------------------------------------------ #
'''
# This REPL will ensure that the user enters a valid choice
# and will output a message accordingly.

valid_yes = ['yes', 'y', 'yep']
valid_no = ['no', 'n', 'nope']

valid_choices = []
valid_choices.extend(valid_yes)
valid_choices.extend(valid_no)


while True:
    print("\nWelcome to the game!")

    # other code ...

    # ask the user if they want to play again
    again = input('Do you want to play again? y/n: ')


    # check to make sure the user has entered a valid choice, using another REPL
    # loop until the user enters a valid choice for the 'again' variable
    while again not in valid_choices:
        print("\nInvalid selection!")
        print(f"Valid choices: {', '.join(valid_choices)}") # display the choices to the user
        again = input("Please enter a valid selection: ")

    # once the code reaches this point,
    # the user is guaranteed to have entered a valid choice

    # check which list contains the user's choice
    if again in valid_yes:
        print("\nOkay, let's play again!")

    elif again in valid_no:
        print("\nGoodbye!")
        break
'''

# ------------------------------------------------------------------------------------- #

# Functions

# named code blocks that perform specific tasks
# take in data, manipulate it and return the result to where the function was called
# must be executed with parentheses after their name

# keyword 'def' to define a function

# variables in the parentheses in the function's definition are called 'parameters'
# parameters are empty variables, awaiting data (can also be given default values)
def multiply(a, b):
    return a * b


# define a variable using the sum of the
# return values from two function calls
product_sum = multiply(2, 10) + multiply(2, 3)
# print(product_sum) # 26

# A function call is equal to its return value
# print(multiply(2, 10) == 20) # True

# 'arguments' must be passed to fill parameters if no default values are provided
# multiply() # TypeError: multiply() missing 2 required positional arguments: 'a' and 'b'

# ----------------------------------------------------------------------------------------- #

def punctuate(text='Hi', punctuation='.'):
    return text + punctuation

# print(punctuate('Hello', '!!!')) # Hello!!! (text='Hello', punctuation='!!!')
# print(punctuate('Goodbye')) # Goodbye. (text="Goodbye", punctuation=default)
# print(punctuate()) # Hi. (text=default, punctuation=default)
# print(punctuate(punctuation='???')) # Hi??? (text=default, punctuation='???')

# ------------------------------------------------------------------------------------------ #

# Return True/False based on whether the 'number' is positive or not
# this function has two return statements, but will only run one or the other
def is_positive(number):
    if number <= 0:
        return False
    else:
        return True


# print(is_positive(-9)) # False
# print(is_positive(9)) # True

'''
# Display different messages for positive and negative numbers
x = 10

if is_positive(x): # == True: (optional)
    print(f"{x} is positive")
else:
    print(f"{x} is negative")
'''
# ------------------------------------------------------------------------------------------- #


def generate_random_numbers(k, low=0, high=100):
    # create a blank list to store the numbers
    numbers = []

    # loop 'k' times
    for x in range(k):
        # generate a random number between 'low' and 'high'
        random_number = random.randint(low, high)

        # add the number to the list
        numbers.append(random_number)

    return numbers

numbers = generate_random_numbers(100, -100, 100)

# process all the numbers in the list and count all the positive numbers:

# set the initial total to 0
total_positive = 0

# loop through all the numbers and count the positive numbers
for number in numbers:
    # if the return value from is_postive() is True
    if is_positive(number):
        # add one to the total
        total_positive += 1


# print(f"There are {total_positive} positive numbers in the list")
# print(f"There are {100 - total_positive} negative numbers in the list")

# ------------------------------------------------------------------- #
# Scope - Four 'layers' in which variables exist

# built-in, global, enclosed, local

# Built-in scope = all built in functions, error messages, etc

x = 'global scope'

def outer_function():
    x = 'enclosed scope'

    def inner_function():
        x = 'local scope'

        return x

    x = inner_function()

    return x
x = outer_function()

# print(x) # local scope


# ---------------------------------------------------------------------------------- #


numbers = []

'''
# Don't do this
def add_number_to_list(number):
    # Since the numbers list isn't being passed 
    # through the parameters, it is confusing 
    # because it's not obvious where the numbers
    # variable is coming from 
    numbers.append(number)
'''



'''
# Do this instead
def add_number_to_list(number, numbers):
    # Now it is obvious where the numbers variable
    # is coming from. It is passed through the 
    # parameters, manipulated and returned 
    numbers.append(number)
    return numbers
'''