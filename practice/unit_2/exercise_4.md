# Exercise 4 - Calculator

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

## 4.1

---

Let's write a REPL (read, evaluate, print, loop) calculator that can handle addition and subtraction. 

Ask the user for an `operator` and each `operand`. Don't forget that `input` returns a `string`, which you can convert to a float using `float(user_input)` where `user_input` is the string you got from `input`. 

Create a separate function for each operation which takes in both `operands` and `returns` the `result` of its operation. 

Pass the user's `operands` to the appropriate function based on the user's selected `operator` and use the value the function returns as your `result`.

Below is some sample input/output.

```
Enter the operation you would like to perform or 'done' to quit: +
Enter the first operand: 1
Enter the second operand: 2

1.0 + 2.0 = 3.0

Enter the operation you would like to perform or 'done' to quit: -
Enter the first operand: 100
Enter the second operand: 25

100.0 - 25.0 = 75.0

Enter the operation you would like to perform or 'done' to quit: done

Goodbye!
```
---
## 4.2

Add functionality for multiplication `*` and division `/`

---
## 4.3

Allow the user to have a running total, each command will perform an operation on that number.

```
Enter the operation you would like to perform or 'done' to quit: +
Enter the first operand: 1
Enter the second operand: 02
1.0 + 2.0 = 3.0

Enter the operation you would like to perform or 'done' to quit: +

3.0 + x:

Enter x: 50

3.0 + 50.0 = 53.0


Enter the operation you would like to perform or 'done' to quit: -

53.0 - x:

Enter x: 7

53.0 - 7.0 = 46.0


Enter the operation you would like to perform or 'done' to quit: done

Your final total was: 46.0

Goodbye!
```

## 4.4

Use a dictionary rather than if/elif to decide which function should be called.

### Exercise 4 [solution](solutions/exercise_4_solution.md)

---

## [< Exercise 3](exercise_3.md) 

### [<< Back to Unit 2 Practice](/practice/unit_2/)