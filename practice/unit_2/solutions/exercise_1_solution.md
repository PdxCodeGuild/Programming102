# Unit 2 Practice Solutions

## **Exercise 1**

### **1.1 Solution**

```python
# create a counter variable to
# to count loop iterations
counter = 0

# begin a REPL
while True:
    # count the current iteration
    counter += 1

    # ask the user if they want the run the loop again?
    again = input('Again? yes/no: ')

    # if the user enters 'no'
    if again == 'no':
        # tell the user how many times the loop ran
        print(f'The loop ran {counter} times.')

        # end the loop
        break
```

## Keep in mind that this is just one potential solution.

## [< Exercise 1](../exercise_1.md) | [Exercise 2 >](../exercise_2.md)

### [<< Back to Unit 2 Practice Problems](/practice/unit_2/)
