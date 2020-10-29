# <a id="top"></a>Unit 2 - Functions

---

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

### Table of Contents

- [REPL](#repl)
- [What is a Function](#whatis)
- [Defining a Function](#define)
- [Passing Arguments to Functions](#arguments)
- [Return](#return)
- [main( )](#main)
- [Exercises](https://github.com/PdxCodeGuild/Programming102/blob/master/practice/unit_2/)
- [Lab 2](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab2.md)

---

## <a id="repl"></a>REPL

- **Read:** take user input
- **Evaluate:** evaluate the input
- **Print:** shows the output to user
- **Loop:** repeat

```python
    play_again = "yes"
    while play_again == "yes":
        # Do some stuff
        play_again = input("Would you like to play again? ")
```

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

- Now we can see what the output would look like if we do not pass in any data:

```python
    my_func()
```

> "Hello"

- And if we do pass in data:

```python
    my_func("Nice day today!")
```

> "Nice day today!"

---

## <a id="return"></a>Return

- Variables and data used inside a function are unique to that function.
- If I declare a variable inside a function, it will only exist inside that function.
- So how do we get the data back out? We use the `return` keyword

```python
    def add(num1, num2):
        '''This function will add two numbers together and return the result'''
        num = num1 + num2
        return num

    added_nums = add(3, 4)
    print(added_nums)
```

In this case our output would be:

> 7

---

## <a id="define"></a>main( )

- It is good practice to use a main function. This is where the core functionality of your code will live.
- Using a main function also helps us keep code clean and helps us avoid using global variables
- Using a main function is similar to using any other function
- First we define the function:

```python
    def main():
        '''This is our main function'''

        # All of our code goes here

```

- Then we just need to call that main function

```python
    main()
```

- Just keep in mind if you define other functions, you define them before your main function.

---

### [Exercises](https://github.com/PdxCodeGuild/Programming102/blob/master/practice/unit_2)

### [Lab 2](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab2.md)

[Back to top](#top)
