# <a id="top"></a>Unit 1 - Review

---

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

### Table of Contents

- [Variables](#variables)
- [DataTypes](#datatypes)
- [Conditional Statements](#conditionals)
- [For / While Loops](#loops)
- [Troubleshooting](#troubleshooting)
- [Exercise 1](https://github.com/PdxCodeGuild/Programming102/blob/master/exercises/exercise1.md)
- [Lab 1](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab1.md)

---

### <a id="variables"></a> Variables

- Variables in python are used to reference data. They make our code more readable if used correctly.
- Variables are declared when you give them a name and assign them a value `name = "Anthony"`
- Keep in mind there are a few rules when choosing your variable name:
  - Variables names are case sensitive (name and NAME are different variables)
  - Must start with a letter or underscore
  - Can have numbers but can not start with one

---

### <a id="datatypes"></a> DataTypes

| DataType | Description            | Example                                       |
| -------- | ---------------------- | --------------------------------------------- |
| String   | Text Surrounded By ""  | `string1 = "hello"`                           |
| Integer  | Whole Number           | `int1 = 4`                                    |
| Float    | Decimal Number         | `float1 = 2.4`                                |
| Boolean  | True/False             | `bool1 = True`                                |
| List     | Collection of Elements | `list1 = ["hello", "goodbye", 4, 2.4, False]` |

---

### <a id="conditionals"></a> Conditional Statements

We can decide `if` we want code to run based on a true or false condtion.

```python
    num = 4
    if num > 0:
        print("Number is greater than zero")
```

We can also choose to run code if the previous condition was false, but the current condion is true.
To do this we use `elif`:

```python
    num = 4
    if num > 0:
        print("Number is greater than zero")
    elif num == 0:
        print("The number is zero)
```

Finally we can use `else` to catch anything that was not caught by the previous condtions:

```python
    num = 4
    if num > 0:
        print("Number is greater than zero")
    elif num == 0:
        print("The number is zero")
    else:
        print("The number is less than zero")
```

---

### <a id="loops"></a> For / While Loops

Loops can be used to run a block of code more than once. Python has two kinds of loops, the `while` loop and the `for` loop.

#### while loops

`while` loops are similar to `if` statements. They run as long as the condition remains true.

```python
    num = 0
    while num < 5:
        print(num)
        num += 1    # Be sure to increment our counter, otherwise the condition would remain True forever
```

#### for loops

`for` loops are slightly different. They are useful when iterating over a list:

```python
    colors = ["red", "blue", "green", "yello", "purple"]
    for color in colors:                                    # color is a temporary variable name holding an element from colors
        print(color)
```

### <a id="troubleshooting"></a> Troubleshooting

![troubleshooting](https://github.com/PdxCodeGuild/Programming102/blob/master/resources/troubleshooting.jpeg)

### [Exercise 1](https://github.com/PdxCodeGuild/Programming102/blob/master/exercises/exercise1.md)

### [Lab 1](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab1.md)

[Back to top](#top)
