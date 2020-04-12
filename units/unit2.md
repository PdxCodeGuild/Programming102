# <a id="top"></a>Unit 2 - Functions

---

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

### Table of Contents

- [What is a Function](#whatis)
- [Defining a Function](#define)
- [Passing Arguments to Functions](#arguments)

---

## <a id="whatis"></a>What is a function?

- A function is a named block of code that runs only when called.
- They are typically designed to do one specific job.
- Once defined, you can call a function as many times as needed.
- You can think of them as a variable, but for a whole block of code!

---

## <a id="define"></a>Defining a function

- Functions are defined (or created) by using the `def` keyword.

```python
    def my_func():
        "This is where the body of the function goes"
```

- As we see above, we use the `def` keyword followed by our functions name `my_func`.
- Notice how the function body is indented. Python uses indentation instead of `{ }` or `( )` like other languages.
- The body is how we tell the computer what `my_func` does.
- It is good practice to use docstrings to tell the user what the function does. Docstrings start and end with triple quotes.

```python
    def my_func():
        '''This is a docstring, use this to tell other users what this function does'''

        print("The function body goes below the docstring")
```

- Now that we have defined a function, in order to use it we need to call that function.

```python
    my_func()
```

---

## <a id="define"></a>Passing Arguments to Functions

- We can pass information into our function and have it do something with that data.
- This requires us to change our function definition slightly.

```python
    def my_func(message):
        '''This function will print a message'''
        print(message)
```

- Now that we have told our function to expect some data, we just pass in the data when we call the function.

```python
    my_func("Hello World")
```

- The data `"Hello World"` is being passed in to our function call.
- That data is then stored in the variable `message`.
- If we run this function, our output would be: `Hello World`.
- You can declare as many arguments in your function defintion as you want.

- You can even declare default values to the variables we create.
- Using defaults is a good way to avoid errors in your code.

```python
    def my_func(message="Hello"):
        '''This function will print a message'''
        print(message)
```
