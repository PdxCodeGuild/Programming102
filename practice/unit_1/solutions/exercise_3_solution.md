# Unit 1 Practice Solutions

## **Exercise 3**

**Problem:**

```python
print 'The last letter of 'elephant' is: {'elephant'[8]}')
```

**Solution:**

1.  `SyntaxError: Missing parentheses in call to 'print'. Did you mean print('The last letter of 'elephant' is: {'elephant'[8]}'))?`

    Missing open parenthesis on `print()`

2.  `SyntaxError: invalid syntax`

    Python is having trouble processing the single quotes around `'elephant'` because the string is created using single quotes. This can be solved by either switching the quotes around elephant to double quotes `"elephant"` or by using _escape characters_ to include the single quotes.

3.  `SyntaxError: invalid syntax`

    This problem is the same as **2.**, except with the next `'elephant'` string. Use double quotes instead.

4.  No error message is raised, but the output is not correct

        The last letter of "elephant" is: {"elephant"[8]}

    In order to have the value for `"elephant"[8]` print in the output, the string in the `print()` needs to be an f-string. Simply add a 'f' before the opening quotation mark.

5.  `IndexError: string index out of range`

    'Elephant' is 8 letters long, but the positions of letters in a string start at 0. Therefore, the characters in 'elephant' are 0 - 7, making the last letter of 'elephant' at position 7.

**Final code:**

```python
print (f'The last letter of "elephant" is: {"elephant"[7]}')
```

**Output:**

    The last letter of "elephant" is: t

---

## [< Exercise 3](../exercise_3.md)

### [<< Back to Unit 1 Practice Problems](/practice/unit_1/)
