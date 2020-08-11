# Unit 2 Practice

## Exercise 2 - Get Colors

### **2.1**

Create a blank list called `colors`.

Construct a Read, Evaluate, Print, Loop (REPL) which performs the following on each iteration of the loop:

- Prompt the user for a `color`
- If the user enters 'done' instead of a `color`, exit the loop.
- If the `color` is already in the `colors` list, inform the user that the color is already in the list and repeat the loop.
- If the color is not already in the `colors` list, add it and tell the user it was added.

When the loop ends, display the list of `colors` back to the user.

    Enter a color or 'done' to quit: blue

        'blue' added to the colors list!

    Enter a color or 'done' to quit: red

        'red' added to the colors list!

    Enter a color or 'done' to quit: purple

        'purple' added to the colors list!

    Enter a color or 'done' to quit: blue

    Oops! 'blue' is already in the colors list!

    output:
    The colors you entered were: blue, red, purple

### **2.2**

Define a function `get_color()` which prompts the user for a `color` and then `returns` that `color`.

Use `get_color()` in your REPL to get the colors from the user.

### Exercise 2 [solution](solutions/exercise_2_solution.md)

---

## [< Exercise 1](exercise_1.md) | [Exercise 3 >](exercise_3.md)

### [<< Back to Unit 2 Practice](/practice/unit_2/)