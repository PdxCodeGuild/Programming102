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

# named code blocks that perform specific tasks
# take in data, manipulate it and return the result to where the function was called
# must be executed with parentheses after their name

# keyword 'def' to define a function

# variables in the parentheses in the function's definition are called 'parameters'
# parameters are empty variables, awaiting data (can also be given default values)
def multiply():
    pass

# define a variable using the return value from the function

# define a variable using the sum of the
# return values from two function calls



# A function call is equal to its return value


# 'arguments' must be passed to fill parameters if no default values are provided


# ----------------------------------------------------------------------------------------- #

def punctuate():
    pass

# ------------------------------------------------------------------------------------------ #

# Return True if the 'number' is between 'low' and 'high'. Otherwise return False.
def is_in_bounds(number, low, high):
    pass



# display different messages if the number is in bounds or not

# ------------------------------------------------------------------------------------------- #

### THIS CAN BE SKIPPED, IF NEEDED

def generate_random_numbers():
    pass

# process all the numbers in the list and count all the numbers that are in a particular range:


# ------------------------------------------------------------------- #
### THIS CAN BE SKIPPED IF NEEDED

# Scope - Four 'layers' in which variables exist

# built-in, global, enclosed, local

# Built-in scope = all built in functions, error messages, etc


# ---------------------------------------------------------------------------------- #
### THIS CAN BE SKIPPED IF NEEDED

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