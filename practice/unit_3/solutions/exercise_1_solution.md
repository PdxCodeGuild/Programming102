# Unit 3 Practice Solutions

## **Exercise 1 Solution**

### **1.1**

```python
fruits = {
    'apple': .65,
    'banana': .5,
    'guava': .33
}

# Display the price of a fruit
print(f"Apples cost ${fruits['apple']} each")

# Add a fruit to the dictionary, print the dictionary to verify its creation

# add 'grapes
fruits['grapes'] = .99
print(f"Added 'grapes': {fruits}")

# Remove a fruit from the dictionary, print the dictionary to verify its deletion

# delete the key:value pair at 'banana'
del fruits['banana']
print(f"Removed 'banana': {fruits}")
```

Output:

    Apples cost $0.65 each
    Added 'grapes': {'apple': 0.65, 'banana': 0.5, 'guava': 0.33, 'grapes': 0.99}
    Removed 'banana': {'apple': 0.65, 'guava': 0.33, 'grapes': 0.99}

### **1.2**

```python
fruits = {
    'apple': .65,
    'banana': .5,
    'guava': .33
}

# display the header label
print("  Fruits  ")
print("----------")

# loop through the keys in the fruits dictionary
fruit_names = fruits.keys()
for fruit_name in fruit_names:

# get the price of the fruit using its name as the key
price_per = fruits[fruit_name]

# print the item
print(f'{fruit_name}: {price_per}')
```

**Output:**

      Fruits
    ----------
    apple: 0.65
    banana: 0.5
    guava: 0.33

### **1.3**

**The Code:**

```python
# fruits and their prices per item
fruit_prices = {
    'apple': .65,
    'banana': .5,
    'guava': .33
}

# fruits in the basket and their quantities
shopping_basket = {
    'apple': 4,
    'banana': 6,
    'guava': 8
}

# set the grand_total to zero
grand_total = 0

# loop through each fruit in the basket
for fruit in shopping_basket:

    # get the quantity of the current fruit
    quantity = shopping_basket[fruit]

    # calculate the sub_total for current fruit
    sub_total = quantity * fruit_prices[fruit]

    # add the sub_total for the current
    # fruit to the grand total
    grand_total += sub_total

    # print the sub_total for the current fruit
    print(f'{quantity} {fruit.capitalize()}s: ${sub_total}')

print("-------------")
print(f'Grand Total: ${grand_total}')
```

**Output:**

    4 Apples: $2.6
    6 Bananas: $3.0
    8 Guavas: $2.64
    -------------
    Grand Total: $8.24

Keep in mind that this is just one potential solution.

## [< Exercise 1](../exercise_1.md) | [Exercise 2 >](../exercise_2.md)

---

### [<< Back to Unit 3 Practice](/practice/unit_3/)
