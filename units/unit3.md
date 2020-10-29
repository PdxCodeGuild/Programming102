# <a id="top"></a>Unit 3 - Dictionaries

---

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

### Table of Contents

- [Dictionaries](#dictionaries)
- [Dictionary Methods](#methods)
- [Looping with Dictionaries](#loops)
- [Exercises](https://github.com/PdxCodeGuild/Programming102/blob/master/practice/unit_3/)
- [Lab 3](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab3.md)

---

## <a id="dictionaries"></a>Dictionaries

- Dictionaries are one of the most powerful datatypes in Python.
- They can be used to store large amounts of data and make working with data easy.
- Dictionaries are a collection of `key: value` pairs
- We can start with an empty dictionary:

```python
    employee_availability = {}
```

- Or we can start with some pre defined data:

```python
    employee_availability = {
    "lisa": "Mon", # string
    "al": ["Tues", "Wed", "Thurs"], # list
    "anthony": ["Mon", "Tues", "Wed", "Thurs", "Fri"] # list
    }
```

- The keys in our employee_availability dictionary are `lisa, al, and anthony`
- The values in our employee_availability dictionary are `"Mon", ["Tues", "Wed", "Thurs"], ["Mon", "Tues", "Wed", "Thurs", "Fri"]`

- To access a value in our dictionary we just need to use the key

```python
    schedule = employee_availability["al"]
    print(schedule)
```

> ["Tues", "Wed", "Thurs"]

- We can change a value by also using a key:

```python
    employee_availability["al"] = ["Mon", "Wed", "Fri"]
    schedule = employee_availability["al"]
    print(schedule)
```

> ["Mon", "Wed", "Fri"]

- To add a new value, we just need to give our dictionary a new key, then assign it a value:

```python
    employee_availability["bill"] = ["Mon", "Wed", "Fri"]
    print(employee_availability)
```

> {"lisa": "Mon", "al": ["Mon", "Wed", "Fri"], "anthony": ["Mon", "Tues", "Wed", "Thurs", "Fri"], "bill": ["Mon", "Wed", "Fri"]}

- To remove a key value pair from a dictionary we use the `del` keyword

```python
    del employee_availability["bill"]
    print(employee_availability)
```

> {"lisa": "Mon", "al": ["Mon", "Wed", "Fri"], "anthony": ["Mon", "Tues", "Wed", "Thurs", "Fri"]}

---

## <a id="methods"></a>Dictionary Methods

Methods give datatypes more functionality, and just like [string methods](https://www.w3schools.com/python/python_ref_string.asp) and [list methods](https://www.w3schools.com/python/python_ref_list.asp), we also have [dictionary methods](https://www.w3schools.com/python/python_ref_dictionary.asp).

| method   | description                                                               | example                                      |
| -------- | ------------------------------------------------------------------------- | -------------------------------------------- |
| clear()  | Removes all elements from a dictionary                                    | dictionary_name.clear()                      |
| copy()   | Returns a copy of the dictionary                                          | new_dictionary = dictionary_name.copy()      |
| get()    | Returns the value of a specified key, or a default value if key not found | data = dictionary_name.get("key", False)     |
| items()  | Returns a list containing key: value pairs                                | data = dictionary_name.items()               |
| keys()   | Returns a list contianing a list of keys                                  | keys = dictionary_name.keys()                |
| pop()    | Removes the element with the specified key                                | dictionary_name.pop("key")                   |
| update() | Updates the dictionary with the specified key: value pairs                | dictionary_name.update({"key": "new value"}) |
| values() | Returns a list of all the values                                          | values = dictionary_name.values()            |

---

## <a id="loops"></a>Looping with Dictionaries

Since dictinaries can become quite large, Python allows us to loop over them.
There are two was to loop over a dictionary:

- The first is to loop over the keys

```python
    for key in employee_availability:
        print(key)
```

```python
> "lisa"
> "al"
> "anthony"
```

- The second is to loop over both the keys and values using the .items() method

```python
    for key, value in employee_availability.items():
        print(key, value)
```

```python
> "lisa" "Mon"
> "al" ["Mon", "Wed", "Fri"]
> "anthony" ["Mon", "Tues", "Wed", "Thurs", "Fri"]
```

### [Exercises](https://github.com/PdxCodeGuild/Programming102/blob/master/practice/unit_3/)

### [Lab 3](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab3.md)

[Back to top](#top)
