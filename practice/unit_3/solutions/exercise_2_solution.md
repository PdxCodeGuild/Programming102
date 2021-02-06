# Unit 3 Practice Solutions

## **Exercise 1 Solution**

### **1.1**

```python
def main():
    # dictionary of tile scores
    scrabble = {
        'BLANK': 0,
        'A': 1,
        'B': 3,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 2,
        'H': 4,
        'I': 1,
        'J': 8,
        'K': 5,
        'L': 1,
        'M': 3,
        'N': 1,
        'O': 1,
        'P': 3,
        'Q': 10,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 1,
        'V': 4,
        'W': 4,
        'X': 8,
        'Y': 4,
        'Z': 10,
    }


    # get the tiles from the user and uppercase them
    tiles = input('Please enter the letters on your tiles, separated by commas: ')

    # replace spaces with blank strings
    # convert all to uppercase
    tiles = tiles.replace(' ', '').upper()

    # split into a list at the commas
    tiles = tiles.split(',')

    # loop through the tiles and add up the point values
    total = 0
    for tile in tiles:
        # get the point value for the current tile
        point_value = scrabble[tile]
        # add the point value to the total
        total += point_value

    # place a comma and a space between each element in tiles and print the result
    result = f"With the letters {', '.join(tiles)} the maximum possible score is {total} if all the tiles are played."

    print(result)


main()
```

Output:

    Please enter the letters on your tiles, separated by commas: blank,g,h,q,z,j,x

    With the letters BLANK, G, H, Q, Z, J, X the maximum possible score is 42 if all the tiles are played.

### **1.2**

```python
def main():
    # dictionary of tile scores
    scrabble = {
        'BLANK': 0,
        'A': 1,
        'B': 3,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 2,
        'H': 4,
        'I': 1,
        'J': 8,
        'K': 5,
        'L': 1,
        'M': 3,
        'N': 1,
        'O': 1,
        'P': 3,
        'Q': 10,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 1,
        'V': 4,
        'W': 4,
        'X': 8,
        'Y': 4,
        'Z': 10,
    }

    tile_quantities = {
        'A': 9,
        'B': 2,
        'C': 2,
        'D': 4,
        'E': 12,
        'F': 2,
        'G': 3,
        'H': 2,
        'I': 9,
        'J': 1,
        'K': 1,
        'L': 4,
        'M': 2,
        'N': 6,
        'O': 8,
        'P': 2,
        'Q': 1,
        'R': 6,
        'S': 4,
        'T': 6,
        'U': 4,
        'V': 2,
        'W': 2,
        'X': 1,
        'Y': 2,
        'Z': 1,
        'BLANK': 2,
    }

    # get the tiles from the user and uppercase them
    tiles = input(
        'Please enter the letters on your tiles, separated by commas: ')

    # replace spaces with blank strings
    # convert all to uppercase
    tiles = tiles.replace(' ', '').upper()

    # split into a list at the commas
    tiles = tiles.split(',')

    # loop through the tiles and add up the point values
    total = 0
    for tile in tiles:

        # if the user's entry contains more of a tile than exist in Scrabble, tell the user.
        number_in_hand = tiles.count(tile)
        number_available = tile_quantities[tile]
        if number_in_hand > number_available:
          print(f'There is/are only {number_available} "{tile}" tile(s) in Scrabble. You entered {number_in_hand}.')

          # exit the main() function
          return

        # get the point value for the current tile
        point_value = scrabble[tile]
        # add the point value to the total
        total += point_value

    # place a comma and a space between each element in tiles and print the result
    result = f"With the letters {', '.join(tiles)} the maximum possible score is {total} if all the tiles are played."

    print(result)


main()

```

**Output:**

```
Please enter the letters on your tiles, separated by commas: z,z,z,z,z,z,z

There is/are only 1 "Z" tile(s) in Scrabble. You entered 7.
```

Keep in mind that this is just one potential solution.

## [< Exercise 2](../exercise_2.md)| [Exercise 3 >](../exercise_3.md)

---

### [<< Back to Unit 3 Practice](/practice/unit_3/)
