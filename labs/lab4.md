# <a id="top"></a>Lab 4 - Count Words

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

Let's write a python module to analyze a given text file and display the most frequently used words in the terminal.

You can get sample text [Here](/resources/countwords.txt)

1. Open your file using `with open()`.
1. Make everything lowercase.
1. Split your text file into a list of words.
1. Use a dictionary to keep track of each word and how many times it occurs. You can use the word as a key, and the count as the value.
1. As you loop over you list of words, if the word is not in your dictionary, add it with the value of 1.
1. If the word already exists in your dictionary add 1 to the count.
1. Once you have counted all your words, display the top 10 in the terminal. You can use the following code to accomplish this:

```python
def get_words():
    '''
        This function will read in the file 'countwords.txt'
        and generate a list from all the words.
    '''
    with open("countwords.txt", "r") as file:
        word_list = file.read().split("\n")
    return word_list

def sort_words(word_dict):
    '''
        This function takes in a dictionary and sorts the words
        by their value
    '''
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

def main():
    # Your code goes here

if __name__ == "__main__":
    main()

```
