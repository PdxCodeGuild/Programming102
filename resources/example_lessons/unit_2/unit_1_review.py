'''
Unit 1 Review
'''

'''
Anatomy of an Error Message

File "<FILENAME>.py", line number
    troublesome code (approximately)
                   ^

ErrorType: specific error message
'''

# SyntaxError - something is mistyped
# 4 + # SyntaxError: invalid syntax
# print('hello) # missing quote - SyntaxError: EOL (end of line) while scanning string literal
# print('hello' # SyntaxError: unexpected EOF (end of file) while parsing

# NameError - a variable name was used that isn't defined
# a + b # NameError: name 'a' is not defined
# imaginary_function() # NameError: name 'imaginary_function' is not defined

# IndendationError - horizontal placement is off
'''
x = 5
if x < 10:
    print('hello')
#    print('hey') # (too far left) IndentationError: unindent does not match any outer indentation level
    #  print('howdy') # (too far right) IndentationError: unexpected indent
'''

'''
if x < 10:
    # empty code block - IndentationError: expected an indented block

print('hello')
'''

# TypeError - wrong datatype was used for an operation
# print('5' + 5) # TypeError: can only concatenate str (not "int") to str
colors = ['red', 'green']
# colors() # TypeError: 'list' object is not callable

# IndexError - index doesn't exist in a sequence
# colors[3] # IndexError: list index out of range
# 'abc'[10] # IndexError: string index out of range

# AttributeError - variable or function or method doesn't belong to a piece of data
# 'hello'.append('x') # AttributeError: 'str' object has no attribute 'append'
# [11, 22, 33].capitalize() # AttributeError: 'list' object has no attribute 'capitalize'

# ModuleNotFoundError - trying to import a non-existent module
# import imaginary_module # ModuleNotFoundError: No module named 'imaginary_module'

# ImportError
# from .. import imaginary_module #ImportError: attempted relative import with no known parent package

# ZeroDivisionError - divinding by zero
# 1/0 # ZeroDivisionError: division by zero

# ValueError - improper value passed to a function
# float('fish') # ValueError: could not convert string to float: 'fish'
# int('3.14') # ValueError: invalid literal for int() with base 10: '3.14'

# ------------------------------------------------------- #

"""
import random
# sometimes errors are triggered in a different file and will need to be hunted down
# Line 77 will trigger an error in the random module
# which will cause a 2-message traceback.
random.choice(123)

'''
Traceback (most recent call last):

  File "unit_1_review.py", line 19, in <module>
    random.choice(123)
  File "C:/.../random.py", line 288, in choice

    i = self._randbelow(len(seq))
TypeError: object of type 'int' has no len()
'''
"""

# -------------------------------------------------------- #

# Handling Errors

# keywords: try / except / else / finally

'''
try:
    # try to run the code in this block
    # if an error is raised, it can be caught using 'except'

except ErrorType: # 'ErrorType' will be the specific type of error you wish to catch
    # run this code block if the error is raised

else:
    # run this block if no error was raised in the 'try' block

finally:
    # run this block whether an error was raised or not
'''


'''
x = 100

while True: # infinite loop
    try:
        x = input("Please enter x: ")
        y = input("Please enter y: ")

        # convert the string to float
        y = float(y)

        # divide the numbers
        quotient = x / y

    # multiple except blocks can be used to catch different errors
    except ValueError: 
        # if y can't be converted:
        print(f'Could not be converted to a float: {y}')
    
    except ZeroDivisionError:
        # if the user enters zero for y
        print('Cannot divide by zero!!!')

    else:
        # if no errors occur, print the result of division
        print(f'{x} / {y} = {quotient}')

        break # continue on to rest of code

    finally:
        print('<3 Math! <3)

print('rest of code....')
'''

'''
# Raise our own error
# keyword: raise
color = input('Please enter a color: ')

try: 
    if color == 'green':
        # if the user enters 'green', raise a ValueError
        raise ValueError(f'I don\'t like the color {color}!!!')
except ValueError as error: # save the custom error message in a variable called error
    print(error)

else:
    print(f'I like the color {color}')
'''
