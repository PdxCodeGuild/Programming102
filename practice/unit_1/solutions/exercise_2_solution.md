# Unit 1 Practice Solutions

## **Exercise 2**

**Problem:**

```python
if num < 3
    print('The number is ' + num)
    print(f'{num is less than three')
        prin('thanks for playing!")
```

**Solution:**

1. `SyntaxError: invalid syntax`

   Missing `:` after `if num < 3`.

2. `IndentationError: unexpected indent`

   `prin('thanks for playing!")` is one space too far to the right.

3. `SyntaxError: EOL while scanning string literal`

   Mismatched quotes in `prin('thanks for playing!")`. String starts with a single quote and ends with a double

4. `SyntaxError: f-string: expecting '}'`

   The f-string in the line: `print(f'{num is less than three')` is missing a closing curly bracket after the variable num

5. `NameError: name 'num' is not defined`

   There is no value set for `num`. Define `num` and assign a number to it that will satisfy the condition in the `if` statment

6. `TypeError: can only concatenate str (not "int") to str`

   The value of `num` is an integer, which cannot be concatenated to a string. We need to convert `num` to a string using the `str()` function or by converting the string to an f-string.

7. `NameError: name 'prin' is not defined`

   A 't' is missing from the end of `print()`, preventing the function from being found.

**Final code:**

```python
num = 1
if num < 3:
    # using an f-string
    print(f'The number is {num}')

    # using str()
    # print('The number is ' + str(num))

    print(f'{num} is less than three')

    print('thanks for playing!')
```

**Final output:**

    The number is 1
    1 is less than three
    thanks for playing!

---

## [< Exercise 2](../exercise_2.md)

### [<< Back to Unit 1 Practice Problems](/practice/unit_1/)
