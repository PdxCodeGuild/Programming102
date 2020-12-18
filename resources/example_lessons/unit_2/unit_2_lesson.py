'''
Unit 2

REPL
Functions
'''

'''
R ead
E valuate
P rint
L oop
'''

'''
# REPL
play_again = 'yes' # loop control

while play_again == 'yes':
    # loop this
    # code block

    print('Welcome to the game!')

    play_again = input('\nDo you want to play again? yes/no: ')
'''

# ------------------------------------------ #


'''
while True: # generic infinite loop
    # loop this code block

    print('Welcome to the game!')

    # ask the user if they want to play again
    play_again = input('\nDo you want to play again? y/n: ')

    if play_again == 'n':
        print('Thanks for playing!')
        break # end the loop

    elif play_again == 'y':
        print("Okay, let's play!\n")
'''
# ------------------------------------------------ #

'''
while True:
    # loop this code block


    print("Welcome to the game!")

    # ask the user if they want to play again
    play_again = input('\nDo you want to play again? y/n: ')

    # define valid responses
    valid_yes = ['y', 'yes', 'yep']
    valid_no = ['n', 'no', 'nope']
    valid_responses = valid_yes + valid_no # combine yes and no reponses

    # ensure the user has selected a valid response
    while play_again not in valid_responses:
        print("Invalid selection! Try again!")
        print(f'Please choose from the following options: {valid_responses}')
        play_again = input('\nDo you want to play again? y/n: ')

    # check which list the users response is in
    if play_again in valid_yes:
        print("Okay, let's play!\n")
    elif play_again in valid_no:
        print("Game over!")
        break
'''

# ------------------------------------------------------------------------ #

# FUNctions!!!

'''
Functions

- are named blocks of code
- run only when called upon
- typically designed to perform a singular task
- once defined, can be called as many times as needed
- are like variables that store code blocks instead of single pieces of data
'''

# define a function with the keyword: def

# functions are generally defined at the TOP of the file, after imports but before all other code
'''
def function_name(parameter1, parameter2, etc): # parameters are BLANK variables, waiting for data
    # this code block
    # is run when 
    # the function is 'called'

    # manipulate the parameter data somehow

    # send data back to where the function was called
    return manipulate_paramters

# 'call' the function and save the return in a variable
data_from_function = function_name(argument1, argument2, etc)
'''

def increment(x):
    return x + 1

# call the function with a value for x

# since the function has parameters, they need data
# increment() # TypeError: increment() missing 1 required positional argument: 'x'
result = increment(39) # use 39 as the value for x and save the result of x + 1 in the variable 'result'
# print(result) # 40

# print(40 == increment(39)) # True

n = 0
while n < 10:
    # print(n)

    # pass the current value of x to increment()
    # receive x + 1 as a result
    n = increment(n)


# ----------------------------------- #

# parameters can be given default values in the function definition
def punctuate(text='Hi', punctuation='.'):
    # print(text)
    # print(punctuation)

    return text + punctuation

# arguments must be provided for ALL parameters if the parameters don't have default values
# punctuate() # punctuate() missing 2 required positional arguments: 'text' and 'punctuation'
# punctuate("I don't like spam") # TypeError: punctuate() missing 1 required positional argument: 'punctuation'
# print(punctuate("I don't like spam", '!!!')) # I don't like spam!!!
# print(punctuate("Welcome to Camelot", "???")) # Welcome to Camelot???
# print(punctuate("No strong opinion")) # use default value for punctuation
# print(punctuate()) # uses default values for BOTH parameters

# ------------------------------------------------------------------------ #

# absolute value of a number is how far it is from 0.

# the absolute value of -9 is 9. absolute value of 9 is ALSO 9, because it is also 9 away from 0

def absolute_value(number):
    if number < 0:
        # flip the number's sign to positive
        number *= -1

    return number

# print(absolute_value(-9)) # 9
# print(absolute_value(44)) # 44
# print(absolute_value(-44)) # 44
# print(absolute_value(-191919)) # 191919

