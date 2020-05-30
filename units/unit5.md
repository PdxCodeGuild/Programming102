# <a id="top"></a>Unit 5 - Final

---

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

### Table of Contents

-   [Final Project](#final)
-   [Lab 5](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab5.md)

---

### Congratulations, You made it!

-   The last day of class is finally here! We hope you've enjoyed yourself! Please help us make Programming 102 better by taking this [anonymous survey](https://forms.gle/D7vCyctcqUQFvSeA9).

## <a id="final"></a>Final Project

Let's take a look at a python module called Turtle.

Turtle is a python `module` that allows us to move a virtual turtle around the screen using programming statements. This turtle has a position and a heading. You can find out more information on the turtle module [here](https://docs.python.org/3/library/turtle.html) or on our [lab 5](labs/lab5.md) page.

Here is some code to get you started:

```python
from turtle import *


def draw_square():
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

    done()

def fill_square():
    fillcolor('red')
    begin_fill()

    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

    end_fill()

    done()

def draw_star():
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)

    done()

def square_loop():
    i = 0
    while i < 4:
        forward(100)
        left(90)
        i = i + 1

    done()

def staircase():
    i = 0
    while i < 4:
        forward(100)
        left(90)
        forward(100)
        right(90)
        i = i + 1
    done()

def spiral():
    fillcolor('blue')

    n_sides = 8
    edge_length = 0

    i = 0
    begin_fill()
    while i < 150:
        forward(edge_length)
        right(360/n_sides)
        i = i + 1
        edge_length = edge_length + 1
    end_fill()
    done()

def expanding_star():
    edge_length = 0
    i = 0
    while i < 100:
        forward(edge_length)
        right(144)

        edge_length += 4

    done()

def your_function_here():
    pass


def menu():
    print("Welcome to turtle, select an option below: ")
    choice = input('''
        1) draw square
        2) fill square
        3) draw star
        4) square loop
        5) staircase
        6) spiral
        7) expanding star
        8) your function goes here
    ''')
    return int(choice)


def run_turtle(choice):
    if choice == 1:
        draw_square()
    elif choice == 2:
        fill_square()
    elif choice == 3:
        draw_star()
    elif choice == 4:
        square_loop()
    elif choice == 5:
        staircase()
    elif choice == 6:
        spiral()
    elif choice == 7:
        expanding_star()
    elif choice == 8:
        print('This is where you call your function')


def main():
    running = True
    while running:
        choice = menu()
        run_turtle(choice)

if __name__ == "__main__":
    main()
```

### [Lab 5](labs/lab5.md)

[Back to top](#top)
