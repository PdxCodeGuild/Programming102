# <a id="top"></a>Unit 4 - Modules

---

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

### Table of Contents

- [What is a Module](#whatis)
- [Importing Modules](#import)
- [Creating our own Module](#create)
- [Exercises](https://github.com/PdxCodeGuild/Programming102/blob/master/practice/unit_4/)
- [Lab 4](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab4.md)

---

## <a id="whatis"></a>What is a Module?

- Once our programs start to get larger, it makes sense to break them up in to smaller pieces or multiple files.
- These other python files are modules.
- Modules are just python files that we can import into our code.

---

## <a id="whatis"></a>Importing

- Importing a module is super easy, we just need to use the `import` keyword followed by the file name.

```python
    import random
```

- In this example we are importing random, which is a random.py file on our system.
- We can import any of our python files this way.
- To call a function from that module we use the module_name.function_name

```python
    random.choice()
```

- Alternatively we can impor only the functions we want from a module

```python
    from random import choice, randint
```

- If we import this way, we no longer need the module name to use the function

```python
    num = randint(1, 100)
```

- We can also rename the module within our file by using the `as` keyword

```python
    import random as super_random_file
```

- Or we could just rename the functions from a module

```python
    from random import choice as choosy_mc_chooserson
```

---

## <a id="whatis"></a>Let's create our own module!

### [Exercises](https://github.com/PdxCodeGuild/Programming102/blob/master/practice/unit_4/)

### [Lab 4](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab4.md)

[Back to top](#top)
