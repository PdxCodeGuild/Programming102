'''
Unit 3 - Dictionaries!
'''

'''
Dictionaries

- are one of the most powerful datatypes in Python
- can be used to store large amounts of data and
    make working with that data quick and easy
- are collections of key:value pairs

keys and values are separated with colons, key:value PAIRS are separated with commas
dictionaries are surrounded by curly brackets {}
'''

# blank dictionary
blank_dictionary = {}

# print(blank_dictionary) # {}
# print(type(blank_dictionary)) # <class 'dict'>

example_dict = {'a': 11, 'b':22, 'c':33}

example_dict = {
    # key:value,
    'a':11,
    'b':22,
    'c':33
}

# keys are generally strings
# values can be ANY datatype, including other dictionaries

# pulling the value at a key by placing the key in square brackets
# print(example_dict['a'])
# print(example_dict['b'])
# print(example_dict['c'])

# cannot get the value at a non-existent key
# example_dict['d'] # KeyError: 'd'

vehicle = {
    'make': 'Dodge',
    'model': 'Dakota',
    'year': 2004,
    'color': 'beige',
}

# print(vehicle['make']) # Dodge


# cannot get the value at a non-existent key
# vehicle['features'] # KeyError: 'features'

# new values CAN be added at at keys that don't exist
vehicle['features'] = ['2WD', 'Auto Windows', 'Auto Locks']

# print(vehicle['features'])

# add a feature to the list of features
vehicle['features'].append('A/C')
# print(vehicle)

# item at index 0 of list at key of 'features'
# print(vehicle['features'][0])

# loop through all the features
# for feature in vehicle['features']:
#     print(feature)

# change the value at a key
vehicle['year'] = 1999
# print(vehicle)

# delete a key:value pair with the keyword: del
# del vehicle['model'] # delete the key:value pair at the key 'model'
# print(vehicle)

# ----------------------------- #

# Dictionary methods

# vehicle['for_sale'] # KeyError: 'for_sale'
'''
desired_key = 'make'

# The following does the same a .get():
# check if the key is in the dictionary
if desired_key in vehicle:
    value = vehicle[desired_key]
else:
    value = f"The key '{desired_key}' doesn't exist in the dictionary!"

# print(value)
'''
# .get(desired_key, default_value_if_not_found)
# return the value at the key, if found. Otherwise it will return the default
# the default value is None if not specified
value = vehicle.get('for_sale', f"The key 'for_sale' doesn't exist in the dictionary!")
# print(value)

value = vehicle.get('make', f"The key 'make' doesn't exist in the dictionary!")
# print(value)

# add multiple key:value pairs
# .update(dictionary) adds the key value pairs in the new dictionary to the old dictionary
vehicle.update({
    'for_sale': True,
    'mileage':120000,
})
# print(vehicle)

# .pop(key) removes the key:value pair at the key
vehicle.pop('for_sale')
# print(vehicle)

# -------------------------------------------- #


fruit_prices = {
    'tomato': .55,
    'pumpkin': 1.0,
    'bell pepper': .75,
}

while True:
    # ask the user which fruit they would like to buy
    fruit_name = input('Please enter the name of the fruit you would like or done to quit: ')

    # exit if 'done'
    if fruit_name == 'done':
        print('Goodbye')
        break

    # use the user's input as they key to get the price
    price_per = fruit_prices[fruit_name]

    # ask how many the user wants
    quantity = input(f'How many {fruit_name}s would you like? ')

    # convert to integer
    quantity = int(quantity)

    # calculate the total
    total = quantity * price_per

    print(f'{quantity} {fruit_name} @ {price_per} each - ${total}')
