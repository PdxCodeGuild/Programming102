'''
Unit 3 Review
'''

# dictionaries are defined using curly brackets
# key:value pairs are separated with commas

blank_dictionary = {}

todo = {
    # key: value,
    'title': 'Go grocery shopping',
    'completed': False
}

# dict keys are usually strings
# dict values can be ANY datatype, including other dicts

# ---------------------------------------------------------------------------------- #

# when accessing values with keys,
# the keys go in SQUARE brackets
title = todo['title']
# print(title) # Go grocery shopping

# integers in square brackets generally mean lists
# string in square brackets generally mean dictionaries

# --------------------------------------------------------------------------------- #

# cannot access a value at a non-existant key
# todo['id'] # KeyError: 'id'

# values can be added to keys that don't yet exist
todo['id'] = 1
# print(todo) # 'title': 'Go grocery shopping', 'completed': False, 'id': 1}

# change the value at a key
# the to do has been finished
todo['completed'] = True
# print(todo) # {'title': 'Go grocery shopping', 'completed': True, 'id': 1}

# ----------------------------------------------------------------------------- #

# .pop(key) delete the key:value pair at the key and return it
todo_id = todo.pop('id')
# print(todo_id, todo) # 1 {'title': 'Go grocery shopping', 'completed': True}


# alternative to the .get() method:
key = 'title'
default = f"'{key}' is not a valid key in the dictionary."

# check if the key is in the dictionary before using it
if key in todo.keys():
    value = todo[key]

else:
    value = default

# print(value)

# .get(key, default) - return the value at the key if it exists or the default if it doesn't

key = 'id'
default = f"'{key}' is not a valid key in the dictionary."

value = todo.get(key, default)
# print(value) # 'id' is not a valid key in the dictionary.

# --------------------------------------------------------- #

key = 'title'
default = f"'{key}' is not a valid key in the dictionary."

value = todo.get(key, default)
# print(value) # Go grocery shopping

# ------------------------------------------------------------------------- #

# add items with methods
#.update(new_dictionary) add the new_dictionary to the original

todo.update({
    'id': 1,
    'user': 'KG'
})
# print(todo) # {'title': 'Go grocery shopping', 'completed': True, 'id': 1, 'user': 'KG'}

# ------------------------------------- #

# Display the todo item
todo_display = f"""
{todo['id']}. {todo['title']}
Created by: {todo['user']}
Completed: {todo['completed']}"""

# print(todo_display)

# ---------------------------------------- #

# looping dictionaries
# .keys(), .values(), .items() - access different parts of the a dictionary

# print(todo.keys()) # dict_keys(['title', 'completed', 'id', 'user'])

# loop through keys
for key in todo.keys():
    # get the value at the current key
    value = todo[key]
    # print(f"{key}: {value}")


# -------------------------------------------------------------------------- #

# .values()
# print(todo.values()) # dict_values(['Go grocery shopping', True, 1, 'KG'])
'''
for value in todo.values():
    print(value)
'''

# ----------------------------------------------------------------------- #
# loop through the key:value pairs (items)

# tuple - unchangeable list, uses indices but cannot accept new values
# print(todo.items()) # dict_items([('title', 'Go grocery shopping'), ('completed', True), ('id', 1), ('user', 'KG')])
'''
for item in todo.items():
    key = item[0]
    value = item[1]
    print(f"{key}: {value}")

'''
# -------------------------------------------------------- #

# 'in' to check if a key is in the dictionary
# print('title' in todo.keys())
# print('completed' in todo) # .keys() is optional

# -------------------------------------------------------- #

# instead of multiple, individual todo item dictionaries, create a list of dictionaries instead
todo_1 = {'title': 'Go grocery shopping', 'completed': False, 'id': 1}
todo_2 = {'title': 'Water the garden', 'completed': True, 'id': 2}
todo_3 = {'title': 'Master Python dictionaries', 'completed': False, 'id': 3}


# list of dictionaries
todo_list = [
    {'title': 'Go grocery shopping', 'completed': False, 'id': 1},
    {'title': 'Water the garden', 'completed': True, 'id': 2},
    {'title': 'Master Python dictionaries', 'completed': False, 'id': 3}
]

# list of dictionaries organized vertically
todo_list = [
    {
        'title': 'Go grocery shopping',
        'completed': False,
        'id': 1
    },
    {
        'title': 'Water the garden',
        'completed': True,
        'id': 2
    },
    {
        'title': 'Master Python dictionaries',
        'completed': False,
        'id': 3
    }
]

# pull out one dictionary at a time from the list
# print(todo_list[0]) # {'title': 'Go grocery shopping', 'completed': False, 'id': 1}
# print(todo_list[0]['title']) # Go grocery shopping

# loop through the todo_list
for todo in todo_list:
    # if todo['completed'] == False:
    if not todo['completed']: # same as line 168
        todo_display = f"""
            {todo['id']}. {todo['title']}
            Completed: {todo['completed']}"""

        # print(todo_display)

# ------------------------------------------------------------ #

# nested dictionaries

fruit_prices = {
    'apple': {
        'green': 2.12,
        'yellow': 3.13,
        'red': {
            'price': 4.14,
            'inventory': 100
        }
    },
    'grape': 3.13
}

# print(fruit_prices['apple']) # {'green': 2.12, 'yellow': 3.13, 'red': 4.14}

apple_prices = fruit_prices['apple']
# print(apple_prices['green']) # 2.12

# print(fruit_prices['apple']['green']) # 2.12

# print(fruit_prices['apple']['red']) # {'price': 4.14, 'inventory': 100}
# print(fruit_prices['apple']['red']['price']) # 4.14