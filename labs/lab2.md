# <a id="top"></a>Lab 2 - Number Lists

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

## 2.1

Create a function called `sum_numbers` which will take in a single parameter, `numbers`, which will be passed a list of numbers as an argument when the function is called. 

The function will return the sum of all the numbers in the list.

```
Numbers: [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]

Sum: 53
```
---

## 2.2

Using a Read, Evaluate, Print, Loop (REPL), build a list of numbers by asking the user to enter them one at a time. Add each number to the list.

Once the user enters 'done', ask the user to define the `target` number for the `remove_all` function. 

Call the functions using the values the user provides.

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

Enter a number to remove it from the list: 4

You entered [4, 5, 4, 7, 4, 9]

The sum of the numbers is 28
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