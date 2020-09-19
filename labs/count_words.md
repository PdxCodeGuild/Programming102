# <a id="top"></a>Lab 5 - Count Words

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

Let's write a python module to analyze a given text file and display the most frequently used words in the terminal.

You can get sample text [Here](/resources/countwords.txt)

1. Pass your file name as a string to get_text(file_name).
2. Using the string of text that's returned,
   1. Replace all new line characters with single spaces `' '`
   2. Make everything lowercase
   3. Remove all punctuation
   4. Split your text file at each space character into a list of words
3. Use a dictionary to keep track of each word and how many times it occurs. You can use the word as a key, and the count as the value.
4. As you loop over you list of words, if the word is not in your dictionary, add it with the value of 1.
5. If the word already exists in your dictionary add 1 to the count.
6. Once you have counted all your words, display the top 10 in the terminal. You can use the following code to accomplish this:

```python
def get_text(file_name):
    '''
        This function will read file_name
        and return its contents as a string.
    '''
    with open(file_name, "r") as file:
        text = file.read()
    return text

def most_frequent(word_dict):
    '''
        This function takes in a dictionary and sorts the words
        by their value, then returns a dictionary with the ten most
        frequently occuring words
    '''
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    
    top_ten = []
    
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        top_ten.append(words[i])

    top_ten = dict(top_ten) # convert list of tuples into a dictionary

    return top_ten

def main():
    # Your code goes here


main()

```
