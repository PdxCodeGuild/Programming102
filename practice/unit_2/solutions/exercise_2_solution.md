# Unit 2 Practice Solutions

## **Exercise 2**

### **2.1 Solution**

```python
# create a blank list called colors
colors = []

# begin REPL
while True:

    # prompt the user for a color
    color = input("Please enter a color to add it to the list or enter 'done' to exit: ")

    # If the user enters 'done' instead of a `color`,
    # display the list of colors to the user and exit the loop.
    if color == 'done':

        # display the colors using .join() to
        # place a comma and a space between each color
        print(f"The colors you entered were: {', '.join(colors)}")

        # end the loop
        break

    # If the color is already in the colors list,
    # inform the user that the color is already in the list
    # and repeat the loop
    if color in colors:

        # inform the user the color is in the list
        print(f'The color {color} is already in the list!')

        # go to the top of the loop
        continue

    # If the color is not already in the colors list,
    # add it and tell the user it was added.
    print(f'The color {color} was added to the list!')
    colors.append(color)
```

### **2.2 Solution**

```python
# Define a function get_color()
# which prompts the user for a color
# and then returns that color.
def get_color():
    '''
    Prompt the user for a color. Return the color.
    '''
    color = input("Please enter a color to add it to the list or enter 'done' to exit: ")

    # return the user's color to the
    # line on which get_color() was called
    return color

# create a blank list called colors
colors = []

# begin REPL
while True:
    # call the get_color() to
    # get a color from the user
    color = get_color()

    # If the user enters 'done' instead of a `color`,
    # display the list of colors to the user and exit the loop.
    if color == 'done':

        # display the colors using .join()
        # to place a comma and a space between each color
        print(f"The colors you entered were: {', '.join(colors)}")

        # end the loop
        break

    # If the color is already in the colors list,
    # inform the user that the color is already in the
    # list and repeat the loop
    if color in colors:
        print(f'The color {color} is already in the list!')

        # repeat the loop
        continue

    # If the color is not already in the `colors` list,
    # add it and tell the user it was added.
    print(f'The color {color} was added to the list!')
    colors.append(color)
```

Keep in mind that this is just one potential solution.

---

## [< Exercise 2](../exercise_2.md) | [Exercise 3 >](../exercise_3.md)

### [<< Back to Unit 2 Practice](/practice/unit_2/)
