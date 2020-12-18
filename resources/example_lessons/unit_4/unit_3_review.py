'''
Unit 3 Review
'''

# dictionaries are defined using curly brackets
# key:value pairs are separated with commas

blank_dictionary = {}

to_do = {
    # key:value,
    'title': 'go grocery shopping',
    'completed': False,
}

# when accessing values with keys,
# the keys go in SQUARE brackets
title = to_do['title']
# print(title) # go grocery shopping

# integers in square brackets generally mean lists
# string in square brackets generally mean dictionaries

# values can be added to keys that don't yet exist
to_do['id'] = 1 # add a value at a key
# print(to_do)

# cannot access a value at a non-existant key
# to_do['tags'] # KeyError: 'tags'

# change the value at a key
to_do['title'] = 'Walk the dog'
# print(to_do)

# the to do has been finished
to_do['completed'] = True # yay!
# print(to_do)

'''
# keyword del for deleting key:value pairs
del to_do['id']
print(to_do)
'''

#.get(key, default) return the value at the key if it exists or the default if it doesn't
# default default value is None
tags = to_do.get('tags', 'No tags exist for this to do!')
# print(tags) # No tags exist for this to do!

title = to_do.get('title', 'No title!')
# print(title) # Walk the dog


# alternative to the .get() method:
key = 'tags'
# check if the key is in the dictionary
if key in to_do:
    # use the key to get the value
    value = to_do[key]
# if the key doesn't exist in the dictionary
else:
    value = 'No tags exist for this to do!'

# print(value)


# add items with methods
#.update(new_dictionary) add the new_dictionary to the original
to_do.update({
    'id':1,
    'tags': ['chores', 'pets'],
    'user': 'kg'
})

# print(to_do)

# .pop(key) delete the key:value pair at the key and return it
# tags = to_do.pop('tags') # remove the value at they key 'tags' and save it in the tags variable
# print(tags, to_do)

# ------------------------------------- #

# looping dictionaries
# .keys(), .values(), .items()

# loop through keys (two ways)
for key in to_do.keys():
    output = f'key: {key}'
    # print(output)

for key in to_do: # same as above with .keys()
    # get the value at the current key
    value = to_do[key]
    output = f'{key}: {value}'
    # print(output)

# loop through the values
for value in to_do.values():
    output = f'value: {value}'
    # print(output)

# loop through the key:value pairs (items)
for item in to_do.items():

    # use indices to get the key and value
    key = item[0]
    value = item[1]

    output = f'{key}: {value}'
    # print(output)

# 'unpack' items into TWO separate variables each loop
for key, value in to_do.items():
    output = f'{key}: {value}'
    # print(output)


display = f"""
Created by: {to_do['user']}
Todo #{to_do['id']} - {to_do['title']}
Completed: {to_do['completed']}
tags: {', '.join(to_do['tags'])}
"""

# print(display)


# todo = {'title': 'Go grocery shopping', 'completed': True}
​
# -------------------------------------------------------- #

# list of dictionaries
todos = [
    {'title': 'Go grocery shopping', 'completed': True},
    {'title': 'Walk the dog', 'completed': False},
    {'title': 'Brush teeth', 'completed': True},
]
​
# pull out one dictionary at a time from the list
for todo in todos:
    output = f"{todo['title']}\nCompleted: {todo['completed']}\n"
    # print(output)
​
# ------------------------------------------------------------ #
​
# nested dictionaries
fruits = {
    'banana': .5,
    'apple': {'red': .55, 'yellow': .25, 'green': .45}
}
​
​
apple_prices = fruits['apple']
print(apple_prices['red'])
# same as above:
print(fruits['apple']['red']) # two keys next to each other