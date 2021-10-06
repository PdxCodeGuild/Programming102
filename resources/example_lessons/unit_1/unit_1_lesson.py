'''
Programming 102
Unit 1
'''

"""
Anatomy of an Error Message
---------------------------

Traceback (most recent call last):
    File "<FILENAME>.py", line number (approximate)
        troublesome code (approximate)
                       ^

ErrorType: specific error message
"""

# SyntaxError - a piece of code is missing or misused
# 4 + # SyntaxError: invalid syntax
# 'hello # SyntaxError: EOL (end of line) while scanning string literal (missing closing quote)
"""
print('hello'        # missing closing parenthesis


x = 3
y = 4
"""

# if the carrot is at the beginning of a line, chances are the error is above that line

# ------------------------------------------------------------------------------------------ #

# NameError - a variable or function name is used but isn't defined
# xylophone # NameError: name 'xylophone' is not defined
# imaginary_function() # NameError: name 'imaginary_function' is not defined
# typE() # NameError: name 'typE' is not defined

# ------------------------------------------------------------------------------------------ #

# IndentationError - inconsistent horizontal placement

# too far right - "unexpected indent"
# too far left - "unindent does not match any outer indentation level"

'''
 x = 5 # IndentationError: unexpected indent

if x < 10:
    print('hello')
     print('hello') # IndentationError: unexpected indent
   print('hello') # IndentationError: unindent does not match any outer indentation level

for x in range(10):
    # blank code block
    # keyword 'pass' to avoid a blank code block error
    # pass

print(x) # IndentationError: expected an indented block
'''
