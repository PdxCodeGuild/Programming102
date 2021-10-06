'''
Programming 102
Unit 2
'''

import random

'''
R ead
E valuate
P rint
L oop
'''

### INTRODUCE THE TERMINAL AS A REPL

'''
play_again = 'yes'

# this loop will only loop if the user enters exactly 'yes'
while play_again == 'yes':
    # loop this code block

    print('\nWelcome to the game!')

    # ...
    # ... other code ...
    # ...

    # ask the user if they want to play again
    play_again = input("Do you want to play again? yes/no: ")

else:
    print("\nThanks for playing!")
'''
# ------------------------------------------------------------------------------- #

'''
while True: # infinite loop, requiring 'break' to end the loop
    # ask the user for a color and give them the option to quit
    color = input("\nEnter a color or 'done' to quit: ")

    # check if the user wants to quit
    if color == 'done':
        print('Goodbye!')
        break # end the loop


    print(f"\nThanks for entering '{color}'")
    
'''

# ------------------------------------------------------------------------------------------ #

# Functions!

# built-in functions
# print(), type(), input(), len(), str(), int(), float(), list(), bool(), range()

'''
Functions

- named code blocks
- run only when called upon with parentheses after their name
- typically designed to perform a single task
- once defined, a function can be called as many times as needed with different data
- receive data & return data after it's been manipulated
'''

# ---------------------------------------------------------------------------------- #

### INTRODUCE INCREMENTALLY
### 1. KEYWORD def
### 2. function_name, PARENTHESES, AND COLON
### 3. EXPLAIN THAT THE CODE BLOCK WILL BE CALLED WHEN THE FUNCTION IS RUN
### 4. DEFINE PARAMETERS TO ALLOW DATA TO BE PASSED INTO THE FUNCTION
### 5. EXPLAIN THAT THE DATA THAT IS PASSED TO THE PARAMETERS IS MANIPULATED IN THE FUNCTION
### 6. EXPLAIN return, THE VALUE THAT'S RETURNED AS WELL AS TO WHERE IT'S RETURNED
### 7. CALL THE FUNCTION, PASS ARGUMENTS, DEFINE VARIABLE WITH RETURN VALUE

### 8. THIS FORMAT CAN BE USED TO DEFINE ALL THE OTHER FUNCTIONS TOO

# keyword 'def' to define a function
'''
# parameters are empty variables in a function's definition which await data from the function call
def function_name(parameter_1, parameter_2, ...):
    # this code block will be run
    # when the function is 'called'

    # manipulate the parameters somehow

    # send the result back to where the function was called
    # with the keyword 'return'
    # if no return value is specified, a function will return 'None' by default
    return manipulate_parameters

# call the function and save the return value in a variable
data_returned_from_function = function_name(argument_1, argument_2, ...)
# data passed to functions to fill parameters are called 'arguments'
'''
# ----------------------------------------------------------------------------------- #

# increment(number) - add one to the number and return the result

def increment(number):
    result = number + 1
    return result

# call the function with a value for 'number'
result = increment(9)
# print(result)

result = increment(result)
# print(result)

# use the function in a loop
x = 0

while x < 10:
    # print(x)

    # use the function to increment x
    x = increment(x)

# -------------------------------------------------------------------------------------- #

# arguments MUST be passed to fill parameters (unless default values are provided)
# increment() # TypeError: increment() missing 1 required positional argument: 'number'

# ---------------------------------------------------------------------------------------- #

# add(a, b) - return the sum of two numbers, 'a' and 'b'

def add(a=1, b=1):
    return a + b

# if NO default values are provided for parameters:
# add() # TypeError: add() missing 2 required positional arguments: 'a' and 'b'
# add(9) # TypeError: add() missing 1 required positional argument: 'b'
# print(add(9, 1)) # 10 - a=9, b=1

# if default values ARE provided for parameters
# print(add(10)) # 11 - (a=10, b=default)
# print(add()) # 2 - (a=default, b=default)
# print(add(5, 2)) # 7 - (a=5, b=2)
# print(add(b=7)) # 8 - (a=default, b=7)
# print(add(b=7, a=5)) # 12 - (a=5, b=7)

# ------------------------------------------------------------------------------------- #

# 'shred' a string and return a randomized list of its characters

def shred_string(string):
    # convert the string to a list of its characters
    characters = list(string)

    # randomize the list
    random.shuffle(characters)

    return characters



shredded = shred_string('hello world')
# print(shredded)

shredded = shred_string('ABCDEFG')
# print(shredded)

# -------------------------------------------------------------------------------------- #

# generate a list of 'k' integers between 'low' and 'high'

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


random_numbers = generate_random_numbers(10)
# print(random_numbers) # [80, 94, 71, 99, 3, 48, 74, 29, 41, 12]

random_numbers = generate_random_numbers(3, 10, 20)
# print(random_numbers) # [15, 17, 17]

random_numbers = generate_random_numbers(1000, -100, 100)
# print(random_numbers)

