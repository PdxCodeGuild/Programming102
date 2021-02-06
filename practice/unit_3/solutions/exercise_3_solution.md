# Unit 3 Practice Solutions

## **Exercise 1 Solution**

```python
def days_in_month(month):
    '''Return the number of days in the month'''
    months = {
        'january': 31,
        'february': 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
    }

    # return the value at the given month
    return months[month]


def main():

    while True:
        # ask the user which month
        print("\nEnter the full name of a month to see how many days are in it")
        month = input("or 'q' to quit: ")

        # check if the user wants to quit
        if month == 'q':
            print('\n\tHave a lovely day!')
            break # end the loop

        # call the function to receive the number of days. lowercase the month to match dict keys
        days = days_in_month(month.lower())

        # display the result
        print(f'\n\t{month.capitalize()} has {days} days in it.')
    

main()
```


**Output:**

```
Enter the full name of a month to see how many days are in it
or 'q' to quit: september
    
    September has 30 days in it.

Enter the full name of a month to see how many days are in it
or 'q' to quit: february
    
    February has 28 days in it.

Enter the full name of a month to see how many days are in it
or 'q' to quit: march
    
    March has 31 days in it.

Enter the full name of a month to see how many days are in it
or 'q' to quit: q
    
    Have a lovely day!
```
Keep in mind that this is just one potential solution.

## [< Exercise 3](../exercise_3.md)

---

### [<< Back to Unit 3 Practice](/practice/unit_3/)
