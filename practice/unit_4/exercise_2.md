## Unit 4 Practice

## **Exercise 2 - Hero Battle**

## <div id="1-1">2.1</div>
---
Create two dictionaries, `hero` and `villain`. The items in each dictionary will represent each characters stats.

<div align="center">

|Stat|Datatype|Values|
|-|-|-|
|`name`| string| any|
|`hp`| integer | 0 - 100|
|`attack` | integer |1 - 10|
</div>

<br>
<br>

## `is_defeated()`
The `is_defeated()` function will determine if a player's `hp` is at or below zero, meaning they're been defeated. Here's the function's definition:

```python
def is_defeated(character):
    '''
    Returns False if the character's hp is greater than zero
    Returns True if the character's hp is less than or equal to
    '''
    # ... your code here ...

    pass # replace 'pass' with a return statement
```

<br>
<br>


<br>

Write a REPL which allows the two characters to do battle. Each character will attack during every loop. 

Each attack will subtract the character's `attack` strength from its opponents `hp`. Since the `attack` stat has a range from 1 - 10, **feel free to multiply it by *5* or *10* to speed up the battle.**

Use the `is_defeated()` function to determine if the opponent has lost the battle, announce who won and end the loop.

An `input()` function can be used to slow the battle down a bit and allow the user to decide when the next round of the battle will be executed. This way the battle will be more interactive and won't happen instantaneously.

<br>

### [Exercise 2.1 Solution](./solutions/exercise_2/exercise_2_1_solution.md)

<br>
<br>

## <div id="1-2">2.2</div>
---


Chances are that there is a fair amount of reptition in the logic which performs each character's turn in the battle, since the same steps will need to be executed by each character during their turn.

Create a function `attack()` to handle each round of the battle.

```python
def attack(attacker, opponent):
    '''
    Apply battle damage to the opponent using the attacker's attack stat
    If the opponent is defeated, return True, signifying the battle is over
    Otherwise return False, signifying the battle will continue for another round
    '''
    # ... your code here ... 

    return # use is_defeated() to return True/False if the battle is over
```

Subtract the value of the attacker's `attack` stat from the opponents `hp` stat. Return `True` if the opponent is defeated, otherwise return `False`. This boolean will be used to determine if the battle is over or if it will continue for another round.

<br>

### [Exercise 2.2 Solution](./solutions/exercise_2/exercise_2_2_solution.md)


<br>
<br>

## <div id="1-3">2.3</div>
---


Add additional stats `defense` and `stance` and add allow each the characters to choose their `stance` each round.

<div align="center">


|Stat|Datatype|Values|
|-|-|-|
|`name`| string| any|
|`hp`| integer | 0 - 100|
|`attack` | integer |1 - 10|
|`defense` |integer |1 - 10|
|`stance`| string |`'attack'` / `'defend'`|

</div>

<br>

If a character chooses to defend, they will not attack this turn.

If the character's stance is set to `'defend'` when their opponent attacks, the damage they receive is reduced. If the character's stance is set to `'attack'`, no change is made to the incoming damage.

Two additional functions could be added to handle these modifications:

<br>

## `set_stance()`

This function will take in a character dictionary and allow them to choose whether they want to set their `stance` stat to`attack` or `defend` this round using a REPL.

```python
def set_stance(character):
    '''
    Ask the user which stance they would like to take this round.
    Change the value at the key of 'stance' to match the user's choice.
    Stance options: 'attack', 'defend'
    '''

    # ... your code here ... 

    # return the character dictionary with adjusted stance stat
    return character

```

<br>

## `defend()`

The function `defend()` will be used to adjust the incoming damage to a character when it's their opponent's turn to attack.

Below are the damage reduction rates for different `'defense'` stat levels:

<br>

<div align="center">

|Defense Level|Damage Reduction|
|-|-|
|0 - 4|10%|
|5 - 7|33%|
|8 - 10|66%|

</div>

<br>

```python
def defend(character, incoming_damage):
    '''
    Calculate the amount the incoming_damage will be reduced 
    based on the character's 'defense' stat. 
    
    Return the amount the incoming_damage will be reduced
    in a variable called 'damage_reduction'
   
    0 - 4 = 10%, 5 - 7 = 33%, 8 - 10 = 66%
    '''

    # return the reduction amount, rounded to the nearest integer
    return round(damage_reduction)
```

<br>

### [Exercise 2.3 Solution](./solutions/exercise_2/exercise_2_3_solution.md)


<br>
<br>

---

### <div id="extra-challenge">Extra Challenge</div>

Add some more fun features. Pull from your favorite games or stories and get creative! Some ideas might include:

- Special, stronger attacks. These could even require a few rounds to build up power before they're able to be used. 
- randomized stats
- randomize which character attacks first
- add `'heal'` as a possible `stance` option and increase the character's `hp` that round if chosen based on a `healing` stat
- have the opponent's choices be made by code, rather than user input
- add a third character
- More than one `villain` (list of dictionaries). The `hero` could `level_up()` with each opponent it defeats. 


---

### [<< Back to Unit 4 Practice](/practice/unit_4/)
