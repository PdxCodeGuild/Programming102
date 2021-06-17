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

# ------------------------------------------------------------------------------- #

# This REPL displays different things for 'y','n' and invalid options
# but will loop unless the user enters 'n'

# ------------------------------------------------------------------------------ #

# This REPL will ensure that the user enters a valid choice
# and will output a message accordingly. 

# ------------------------------------------------------------------------------------- #

# Functions

# named code blocks that perform a specific task
# take in data, manipulate it and return the result to where the function was called
# must be executed with parentheses after their name

# keyword 'def' to define a function

# variables in the parentheses in the function's definition are called 'parameters'
# parameters are empty variables, awaiting data (can also be given default values)
def multiply():
    pass

# define a variable using the sum of the
# return values from two function calls

# A function call is equal to its return value

# 'arguments' must be passed to fill parameters if no default values are provided

# ----------------------------------------------------------------------------------------- #

def punctuate():
    pass

# (text="Hello", punctuation="!!!")
# (text="Goodbye", punctuation=default value)
# (text=default, punctuation=default)

# specify which parameter receives which argument
# (text=default, punctuation="???") 
# (punctuation='?!', text='Huwuh')

# ------------------------------------------------------------------------------------------ #

def is_positive():
    pass


# Display different messages for positive and negative numbers
# x = 10


# ------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------------------------- #

def generate_random_numbers():
    pass



# process all the numbers in the list:

# set the initial total to 0

# loop through all the numbers and count the positive numbers
    # if the return value from is_postive() is True
        # add one to the total

# print(f"There are {total} positive numbers in the list")
# print(f"There are {100 - total} negative numbers in the list")

# ------------------------------------------------------------------- #
# Scope - Four 'layers' in which variables exist

# built-in, global, enclosed, local

# Built-in scope = all built in functions, error messages, etc
'''
x = "global scope"

def outer_function():
    x = "enclosing scope"

    def inner_function():
        x = "local scope"
        print(x)
    
    inner_function()

outer_function()
'''

# y = 500

def scope_example():

    # since the function and the variable 'y' are 
    # both defined in the global scope, 
    # 'y' is available within the function
    # print(y) 
    
    x = 1000

    pass


# scope_example()

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