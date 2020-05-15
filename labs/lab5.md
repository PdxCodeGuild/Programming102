# <a id="top"></a>Lab 5 - Vending Machine

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

Let's create a REPL style Vending Machine in Python.

You will need to have a main menu, that displays the options to the user:

-   Display Items
-   Insert Money
-   Purchase Item
-   Return unspent money

For displaying, we will store all of our items in a dictionary where the key is the item and the value is a list where first item is the price and the second item is the quantity.

```python
vending_items = {
    "chips": [.75, 5],
    "candy": [.75, 8],
    "water": [1.0, 2],
    "soda": [1.25, 0]
}
```

You can change out the items, prices or quantities to your liking, this is just an example.

To display all of the options in our vending machine, we can just use the keys

Our next step is to allow the user to enter money, this will need to be a float, with 1 being a dollar and any decimals being cents.

After the user enters their amount, allow them to pick an item. If they entered enough money, subtract one from the total remaing items.

Do not allow them to buy an item if 0 are remaining.

Do not allow them to buy an item if they do not have enough money.

To access the price of "chips" we can use the following syntax:

```python
price = vending_items["chips"][0]
```

By saying `vending_items["chips"]` it will return that list, then we just need to specify the index

Lastly give the user an option to 'return' any unspent money.

## Recomendations:

-   Break this lab down one step at a time, maybe focus on just the menu first, then move on to another part
-   Test as you go, you are more likely to find an error sooner if you test your code frequently
-   Use functions to help break up code
-   Leave comments to explain your code
