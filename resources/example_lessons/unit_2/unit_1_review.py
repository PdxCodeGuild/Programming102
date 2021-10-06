'''
Programming 102
Unit 1 Review
'''
import random


"""
Anatomy of an Error Message
---------------------------

Traceback (most recent call last):
  File "<FILENAME>.py", line number (approx)
    troublesome code (approx)
                   ^

ErrorType: specific error message
"""

# SyntaxError - a piece of code is missing or misused
# 10 / # SyntaxError: invalid syntax
# 'abc # SyntaxError: EOL (end of line) while scanning string literal (missing closing quote)
# print('hello world'] # SyntaxError: closing parenthesis ']' does not match opening parenthesis '('

# ------------------------------------------------------------------------------ #

# NameError - variable or function name was used that isn't defined
# balloon # NameError: name 'balloon' is not defined
# Print() # NameError: name 'Print' is not defined

# ------------------------------------------------------------------------------ #

# IndentationError - inconsistent horizontal placement

# too far right - unexpected indent
# too far left - unindent does not match any outer indentation leve
'''
 x = 4 # IndentationError: unexpected indent

if x < 10:
    print('hello')
   print('hello') # IndentationError: unindent does not match any outer indentation leve
     print('hello') # IndentationError: unexpected indent


for x in range(10):
    # blank code block
    # 
    # keyword 'pass' will avoid empty code block errors

print(x)
'''

# ----------------------------------------------------------------------------- #

# TypeError - wrong datatype was used for an operation
# '5' + 5  # TypeError: can only concatenate str (not "int") to str
# print['hello world'] # TypeError: 'builtin_function_or_method' object is not subscriptable
# [10, 20, 30] / 10 # TypeError: unsupported operand type(s) for /: 'list' and 'int'

# ----------------------------------------------------------------------------- #

# IndexError - index doesn't exist in a sequence (list, string, etc...)
colors = ['red', 'green', 'blue']

# colors[3] # IndexError: list index out of range
# 'abc'[3] # IndexError: string index out of range

# colors[3] = 'purple' # IndexError: list assignment index out of range

# ------------------------------------------------------------------------------ #

# AttributeError - variable, function or method doesn't belong to an object
# random.imaginary_function() # AttributeError: module 'random' has no attribute 'imaginary_function'
# 'abc'.append('d') # AttributeError: 'str' object has no attribute 'append'
# colors.capitalize() # AttributeError: 'list' object has no attribute 'capitalize'

# -------------------------------------------------------------------------------- #

# ValueError - proper datatype, but improper value was used
# int('abc') # ValueError: invalid literal for int() with base 10: 'abc'
# float('abc') # ValueError: could not convert string to float: 'abc'

# ------------------------------------------------------------------------------- #

# ZeroDivisionError - division by 0
# 1/0 # ZeroDivisionError: division by zero

# --------------------------------------------------------------------------------- #

# sometimes errors are triggered in different files and will need to be tracked down

# random.choice(123)

"""
Traceback (most recent call last):
  File "C:/Users/keego/Desktop/pdx_code/programming_102/unit_2/unit_1_review.py", line 93, in <mo
dule>
    random.choice(123)
  File "C:/Users/keego/AppData/Local/Programs/Python/Python39/lib/random.py", line 346, in choice

    return seq[self._randbelow(len(seq))]
TypeError: object of type 'int' has no len()
"""

# -------------------------------------------------------------------------------------------- #

"""
Error Handling
Keywords: try, except, else, finally


try:
    # try to run the code in this block
    # if an error is raised in this block,
    # it can be caught and handled using an 'except' block

except ErrorType:
    # 'ErrorType' is the specific type of error we wish to catch
    # run this code block if the specified ErrorType was raised

else:
    # run this code block if no error occurred in the 'try' block

finally:
    # run this code block no matter what

"""

# ----------------------------------------------------------------------------------------------- #

# Divide two numbers provided by the user. 
# Before dividing, validate that the user has entered proper numbers
'''
while True: # infinite loop, requiring 'break' to end
    try:
        x = input("Enter number for x: ")
        y = input("Enter number for y: ")

        # try to convert the numbers to float
        x = float(x)
        y = float(y)

        # try to divide the numbers
        quotient = x / y

    except ValueError:
        print(f'\nOne of the numbers could not be converted to float: {x}, {y}')

    # multiple except blocks for multiple errors
    except ZeroDivisionError:
        print('\nCannot divide by zero!!!')

    else:
        # if no error was raised
        print(f'\n{x} / {y} = {x / y}')
        break # end the loop once the user enters two valid numbers

    finally:
        print("\nYay, Python!")
        
'''