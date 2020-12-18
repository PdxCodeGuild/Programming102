'''
Unit 2 Review
'''

'''
R ead
E valuate
P rint
L oop
'''

'''
again = 'yes' # loop control
while again == 'yes':
    print('Welcome to the program!')

    # allow the user to redefine the again variable
    again = input("Do you want to play again? yes/no: ")
'''

'''
# REPL with keyword break
while True: # infinite loop
    print('Welcome to the program!')

    again = input("Do you want to play again? y/n: ")

    if again == 'n':
        print("Goodbye!")
        break
'''

'''
# Ask the user for a list of colors with no duplicates
colors = [] # blank list to hold colors
while True:
    # ask the user for a color
    color = input("Please enter a color or 'done' to quit: ")

    # if the user enters 'done', break the loop
    if color == 'done':
        print(f'You entered: {colors}')
        break

    # ensure the user enters a color that isn't in the list
    while color in colors:
        print(f'Color already in the list: {color}')
        color = input("Please enter a color: ")
    
    # once the user enters a color that isn't in the list
    # add it to the list
    print(f'Color added to the list: {color}')
    colors.append(color)
    print(colors)

    # exits at 5 colors
    if len(colors) == 5:
        print(colors)
        break

'''

'''
limit = input('How many numbers do you want to add to the list: ')
limit = int(limit)

numbers = []
for x in range(limit): # while len(numbers) < limit
    number = input('Please enter a number: ')

    # convert number to float
    number = float(number)

    numbers.append(number)
    print(f'{number} added to the list')

print(numbers)
'''

# ------------------------------------------------ #

# Functions

def punctuate(text, punctuation): # variables within parentheses are called 'parameters'
    return text + punctuation

punctuated_text = punctuate("I don't like spam", "!!!") # values in parentheses in the function call are 'arguments'

# print(punctuated_text)

def absolute_value(number):
    if number < 0:
        number *= -1

    return number

# print(absolute_value(-9))
# print(absolute_value(-123123))
# print(absolute_value(123123))

def power_n(number=2, n=0):
    '''Return the number raised to the power of n'''
    return number ** n

# print(power_n(2, 9))
# print(power_n()) # number = 1, n = 0 (both defaults)
# print(power_n(9, 2)) # number = 9, n = 2
# print(power_n(6)) # number = 6, positional argument
# print(power_n(n=6)) # number = 2 (default), n = 6
# print(power_n(n=6, number=4)) # n=6, number=4

num = 6
exp = 6
# print the return from a function within an f-string
# print(f'{num} to the power of {exp} is {power_n(num,exp)}')

# *args (arguments) / **kwargs (keyword arguments)
def show_args_kwargs(*args, **kwargs):
    print(args)

    for arg in args:
        print(arg)

    print(kwargs)

# show_args_kwargs(3.14, 'cat', True, word1 = 'fish', word2 = 'dog', word3='zebra')

# take in any number of numbers and add them together
def add_em_up(*nums):
    '''
    DOCSTRING:
    Return the sum of any arbitritrary number of nums
    '''
    total = 0 # starting total

    # loop through all numbers and add them to the total
    for num in nums:
        total += num

    return total

# print(add_em_up(34, 54, 99, 10, 14, 10, 5, 1919191, 213930493))


# --------------------- #
# SCOPE - 'bubbles' where variables exist
# y is defined in the global scope
y = 99

# add() is defined in the global scope
def add(a, b):
    # print(y)
    
    # y += 1 # UnboundLocalError

    x = 5 # x is defined in the scope of the function add()

    return a + b


# all the way to the left is called the 'global scope'
# print(x) # x only exists inside add()
# print(add(1,2))