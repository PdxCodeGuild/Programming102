# Unit 2 Practice Solutions

## **Exercise 4 - Calculator**

### **4.1**

```python
def add(a, b):
    '''return the sum of two numbers, a and b'''
    return a + b

def subtract(a, b):
    '''return the difference of two numbers, a and b'''
    return a - b


while True:
    # ask the user for the operation
    operation = input("Enter the operation you would like to perform or 'done' to quit: ")

    # check if the user would like to quit
    if operation == 'done':
        print('Goodbye!')
        break # end the REPL

    # get the operands from the user
    operand_1 = input('Enter the first operand: ')
    operand_2 = input('Enter the second operand: ')

    # convert strings to floats
    operand_1 = float(operand_1)
    operand_2 = float(operand_2)

    # check the operation and call appropriate function
    if operation == '+':
        result = add(operand_1, operand_2)
    elif operation == '-':
        result = subtract(operand_1, operand_2)

    # display the result
    print(f'{operand_1} {operation} {operand_2} = {result}')
```
---

### **2.2**

```python

# add these two functions
def multiply(a, b):
    '''return the product of two numbers, a and b'''
    return a * b

def divide(a, b):
    '''return the quotient of two numbers, a and b'''
    return a / b

# ---------------------------------------------------- #

 # add checks for multiplication and division
if operation == '+':
    result = add(operand_1, operand_2)
elif operation == '-':
    result = subtract(operand_1, operand_2)
elif operation == '*':
    result = multiply(operand_1, operand_2)
elif operation == '/':
    result = divide(operand_1, operand_2)

```

---
### **2.3**
```python
def add(a, b):
    '''return the sum of two numbers, a and b'''
    return a + b

def subtract(a, b):
    '''return the difference of two numbers, a and b'''
    return a - b

def multiply(a, b):
    '''return the product of two numbers, a and b'''
    return a * b

def divide(a, b):
    '''return the quotient of two numbers, a and b'''
    return a / b

# initialize the running total to None
total = None

while True:
    # ask the user for the operation
    operation = input("\n\nEnter the operation you would like to perform or 'done' to quit: ")

    # check if the user would like to quit
    if operation == 'done':
        # print final total
        print(f'\nYour final total was: {total}')

        print('\nGoodbye!')
        break # end the REPL

    # if total still contains the value None, get both operands from the user
    # note: this will only be True on the first loop
    if not total:
        # get the operands from the user
        operand_1 = input('Enter the first operand: ')
        operand_2 = input('Enter the second operand: ')

    else:
        # if the total is already defined, set it as the first operand and get the other operand from the user
        operand_1 = total
        operand_2 = input(f'\n{total} {operation} x:\n\nEnter x: ')
        
    # convert strings to floats
    operand_1 = float(operand_1)
    operand_2 = float(operand_2)

    # check the operation and call appropriate function
    if operation == '+':
        total = add(operand_1, operand_2)

    elif operation == '-':
        total = subtract(operand_1, operand_2)

    elif operation == '*':
        total = multiply(operand_1, operand_2)

    elif operation == '/':
        total = divide(operand_1, operand_2)

    # display the result
    print(f'\n{operand_1} {operation} {operand_2} = {total}')
```

---
### **2.4**
```python
def add(a, b):
    '''return the sum of two numbers, a and b'''
    return a + b

def subtract(a, b):
    '''return the difference of two numbers, a and b'''
    return a - b

def multiply(a, b):
    '''return the product of two numbers, a and b'''
    return a * b

def divide(a, b):
    '''return the quotient of two numbers, a and b'''
    return a / b

# dictionary of operators as keys and their respective functions as values
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# begin running total
total = None

while True:
    # ask the user for the operation
    operator = input("\nEnter the operation you would like to perform or 'done' to quit: ")

    # check if the user would like to quit
    if operator == 'done':
        # print final total
        print(f'\nYour final total was: {total}')

        print('\nGoodbye!')
        break # end the REPL

    # if total still contains the value None
    # note: this will only be True on the first loop
    if not total:
        # get the operands from the user
        operand_1 = input('Enter the first operand: ')
        operand_2 = input('Enter the second operand: ')

    else:
        # if the total is already defined, set it as the first operand 
        operand_1 = total
        operand_2 = input(f'\n{total} {operator} x:\n\nEnter x: ')
        
    # convert strings to floats
    operand_1 = float(operand_1)
    operand_2 = float(operand_2)

    # retrieve the function at the key of the chosen operator
    operation = operations[operator]

    # perform the calculation on the total
    total = operation(operand_1, operand_2)
    
    
    # display the result
    print(f'{operand_1} {operator} {operand_2} = {total}')
```
---
Keep in mind that this is just one potential solution.

---

## [< Exercise 3](../exercise_3.md)

### [<< Back to Unit 2 Practice](/practice/unit_2/)
