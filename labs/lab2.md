# <a id="top"></a>Lab 2 - Number Lists

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

## 2.1

We're going to write Python's built-in function, `sum()`, from scratch.

Create a function called `sum` with a single parameter, `numbers`. Call the function and pass a list of numbers as an argument.

The function will add up all the `numbers` in the list and `return` the sum of the `numbers`.

Note: Please do ***not*** use the built-in function `sum()`. The goal is to write that function from scratch.

```
Numbers: [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]

Sum: 53
```
---

## 2.2

Using a Read, Evaluate, Print, Loop (REPL), build a list of numbers by asking the user to enter them one at a time. Add each number to a list.

Once the user enters 'done', pass the list to the `sum` function from version 2.1 and display the sum that's returned.

```
Enter a number or 'done' to quit:
> 4

Enter a number or 'done' to quit:
> 5

Enter a number or 'done' to quit:
> 4

Enter a number or 'done' to quit:
> 7

Enter a number or 'done' to quit:
> 4

Enter a number or 'done' to quit:
> 9

Enter a number or 'done' to quit:
> done

You entered [4, 5, 4, 7, 4, 9]

The sum of the numbers is 33
```
---

## Extra Challenge

Create a function called `remove_all` which takes in two parameters, `numbers` & `target`.

The `numbers` parameter will be passed a list of numbers and the `target` parameter will be passed the number to remove from the list. 

The function will return a new list containing only the numbers that are not the `target` number.

```
Numbers: [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]

Remove: 4
Numbers: [5, 2, 10, 5, 8, 10]

```
