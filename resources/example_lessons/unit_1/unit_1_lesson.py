'''
Programming 102
Unit 1
'''

# Error messages and Troubleshooting

'''
Anatomy of an Error Message
----------------------------

File "<FILENAME>.py", line number of error
    example of problem code (approximately)
                          ^

ErrorType: specific error message
'''


# SyntaxError - something is mistyped
# 4 + # SyntaxError - invalid syntax
# print('hello) # forgot closing quote - SyntaxError: EOL (end of line) while scanning string literal
# print('hello world' # SyntaxError: unexpected EOF (end of file) while parsing

# NameError - variable has been used that isn't defined
# a = b + c # NameError: name 'b' is not defined
# imaginary_function() # NameError: name 'imaginary_function' is not defined

'''
# IndentationError - horizontal placement is incorrect
if 1 < 2:
    print('1 is less than 2')
   print('2 is greater than 1') # IndentationError: unindent does not match any outer indentation level (too far left)
     print('2 is greater than 1') # IndentationError: unexpected indent (too far right)
'''

