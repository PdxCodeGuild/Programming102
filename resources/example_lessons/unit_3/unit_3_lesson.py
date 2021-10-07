'''
Programming 102
Unit 3
'''

'''
Dictionaries ('dict')

- one of the most powerful datatypes in Python
- can be used to store large amounts of data and make accessing that data quick and easy
- collections of key:value pairs
- keys are used to access values

- are defined using curly brackets {}
- keys and values are separated with colons
- key:value pairs are called 'items'
- items are separated with commas
'''

# blank dictionary
blank_dictionary = {}
# print(blank_dictionary, type(blank_dictionary)) # {} <class 'dict'>


# ------------------------------------------------------------------------------- #

# dict keys are generally strings
# dict values can be ANY datatype, including other dictionaries

example_dict = {'a': 11, 'b': 22, 'c': 33}

example_dict = {
    # key: value,
    'a': 11,
    'b': 22,
    'c': 33
}

# print(example_dict) # {'a': 11, 'b': 22, 'c': 33}

# ------------------------------------------------------------------------------- #

# dictionary values are retrieved by placing their keys
# in SQUARE brackets after the dictionary's name

# print(example_dict['a']) # 11
# print(example_dict['b']) # 22
# print(example_dict['c']) # 33

# ---------------------------------------------------------------------------- #

# dictionaries are usually used to group related data

address = {
    "street": "123 Faux St.",
    "city": "Portland",
    "state": "Oregon",
    "zipcode": 123456
}

# print(address['street'])
# print(f"{address['city']}, {address['state']} {address['zipcode']}")

# ------------------------------------------------------------------------------------------ #

book = {
    'title': 'The Hobbit',
    'author': 'JRR Tolkien',
    'pages': 200
}

# print(f"The book {book['title']} has {book['pages']} pages and was written by {book['author']}")

# ----------------------------------------------------------------------------------------- #

# cannot retrieve values at non-existent keys 
# book['characters'] # KeyError: 'characters'

# add a value at the key of 'characters'
book['characters'] = ['Bilbo', 'Gandalf', 'Smaug']
# print(book['characters']) # ['Bilbo', 'Gandalf', 'Smaug']

# add a character to the list
book['characters'].append('Balin')
# print(book['characters']) # ['Bilbo', 'Gandalf', 'Smaug', 'Balin']

# ---------------------------------------------------------------------------------------- #

# change the value at a key
book['pages'] = 199
# print(book)

# ------------------------------------------------------------------------------------------ #

# deleting a key:value pair
# keyword 'del'
# del book['pages']
# print(book)

# ------------------------------------------------------------------------------------------- #

# dictionary methods

# .pop(key) - remove the key:value pair at the key and return the value
pages = book.pop('pages')
# print(pages, book)

# --------------------------------------------------------------------------------------------- #

# .update(new_dict) - add the items from the new_dict to the original dictionary
new_items = {
    'pages': 200,
    'isbn_number': 3456789876598765
}

# book.update(new_items)
# print(book)

# ----------------------------------------------------------------------------------------------- #

# as of Python 3.9, we can use the 'merge' operator

book = book | new_items

# print(book)

# ------------------------------------------------------------------------------------------------ #

# Fruit Stand

fruit_prices = {
    'apple': 2.33,
    'banana': 1.76,
    'peaches': 2.99
}

while True:
    # ask the user which fruit they want to buy
    fruit_name = input("\nPlease enter the name of the fruit you want to buy or 'done' to quit: ")

    # exit if 'done'
    if fruit_name == 'done':
        print("\nThanks for shopping!")
        break # end the loop

    # get the price of the user's fruit_name
    price_per = fruit_prices[fruit_name]

    # ask the use how many they want
    quantity = input("Enter the quantity: ")
    
    # convert the quantity to integer
    quantity = int(quantity)

    # calculate the total
    total = quantity * price_per
    
    print(f'{quantity} {fruit_name} @ ${price_per} each - ${round(total, 2)}')