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

# Handling Errors

# keywords: try / except / else / finally
'''
try:
    # try to run this code block
    number = input('Please enter a number: ')

    number = float(number)

except ValueError:
    # if a ValueError was raised in the try block, 
    # run this block
    print(f'Could not be converted to a float: {number}')

else:
    # if no error was raised in the try block,
    # run this block
    print(f'Successfully converted to float: {number}')

finally:
    # run this block whether an error was raised or not
    print('Yay Python!')
    
'''

'''
dividend = 100

while True: # infinite loop
    try:
        divisor = input("Please enter a number: ")

        # convert the string to float
        divisor = float(divisor)

        # divide the numbers
        quotient = dividend / divisor

    # multiple except blocks can be used to catch different errors
    except ValueError: 
        # if the divisor can't be converted:
        print(f'Could not be converted to a float: {divisor}')
    
    except ZeroDivisionError:
        # if the user enters zero for the divisor
        print('Cannot divide by zero!!!')

    else:
        # if no errors occur, print the result of division
        print(f'{dividend} / {divisor} = {quotient}')

        break # continue on to rest of code

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
