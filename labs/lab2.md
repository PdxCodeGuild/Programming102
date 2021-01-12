# <a id="top"></a>Lab 2 - Simple Calculator

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

## Version 1

---

Let's write a simple REPL (read, evaluate, print, loop) calculator that can handle addition and subtraction. 

Ask the user for an `operator` and each `operand`. Don't forget that `input` returns a `string`, which you can convert to a float using `float(user_input)` where `user_input` is the string you got from `input`. 

Create a separate function for each operation which takes in both `operands` and `returns` the `result` of its operation. 

Pass the user's `operands` to the appropriate function based on the user's selected `operator` and use the value the function returns as your `result`.

Below is some sample input/output.

```
> what is the operation you would like to perform? +
> what is the first number? 5
> what is the second number? 7
> 5 + 7 = 12
> what is the operation you would like to perform? done
> goodbye
```
---
## Version 2

Add functionality for multiplication `*` and division `/`

---
## Extra Challenge 1

Allow the user to have a running total, each command will perform an operation on that number.

```
> what is the starting number? 15
> enter an operation: + 5
> 20
> enter an operation: * 3
> 60
> enter an operation: done
> Your total is 60. Goodbye.
```

---
## Extra Challenge 2

Allow the user to write an expression, alternating the numbers and operators. Evaluate the expression from left-to-right.

```
> What is the expression? 5 + 2 * 2
> 14
```

## Extra Challenge 3

---

Allow the user to write an expression, alternating the numbers and operators. Follow the proper order of operations, evaluating first the exponential, them multiplication and division, then addition and subtraction.

```
> What is the expression? 5 + 2 * 2
> 9
```
