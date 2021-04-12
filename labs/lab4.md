# <a id="top"></a>Lab 4 - Anagram Checker

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

Let's write an anagram checker.

## Anagram

Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. `dormitory` and `dirtyroom`.

Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.

1. Convert the strings into lists
2. Sort the letters of each list
3. Check if the two lists are equal

```
>>> enter the first word: dormitory
>>> enter the second word: dirtyroom
>>> 'dormitory' and 'dirtyroom' are anagrams
```

One potential solution to this lab involves Python's built-in function `sorted()`, which will sort list items as well as characters in a string. However, please use the **list method** for sorting the lists in this lab instead.

# Extra Challenge 1

1. Convert each word to lower case
2. Remove all the spaces from each word by replacing them with empty strings

# Extra Challenge 2

Make your program ignore punctuation when checking anagrams.

# Extra Challenge 3

Let the user enter as many words as they choose. If every word is an anagram of every other word, let the user know.
