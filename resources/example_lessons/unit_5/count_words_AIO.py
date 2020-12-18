from string import punctuation

def sort_by_value(tup):
    '''return the first item of the tuple for sorting'''
    return tup[1]

# open a text file
with open('alice.txt', 'r') as text_file:
    # alice.txt is open ONLY in this code block
    
    # read the file's contents and save to a variable as a giant string
    dirty_text = text_file.read()

# text file is closed here

# clean the text
# lowercase everything
clean_text = dirty_text.lower()

# remove all newline characters
clean_text = clean_text.replace('\n', ' ')

# remove all punctuation
# loop through each punctuation character and remove it from the text
for punct in punctuation:
    clean_text = clean_text.replace(punct, '')


# split the text at each space to form a list of words
word_list = clean_text.split(' ')


# loop through the list of words and count the number of occurance of each

# store the words and their counts in a dictionary
word_counts = {}

# loop through the list of words
for word in word_list:

    # skip all blank strings
    if word == '':
        continue

    # if the word is not a key in the dictionary,
    if word not in word_counts:
        # add it with a value of 1
        word_counts[word] = 1
    
    # if the word IS ALREADY a key in the dictionary,
    elif word in word_counts:
        # add 1 to its value
        word_counts[word] += 1

words = list(word_counts.items())

 # sort the list of tuple items by value in descending order
words.sort(key=sort_by_value, reverse=True)

# empty list for top ten words
top_ten = [] # list slicing - words[0:10] # list_name[start_index:stop_index]

# loop 0 - 9
for index in range(10):
    # add each of the top ten words to the list
    top_ten.append(words[index])

top_ten = dict(top_ten)

# label for output
output = 'Top Ten Words\n-------------\n'

# 'unpack' the word and count for each item into two variables
for word, count in top_ten.items():
    # add the current word and its count to the output string with a new line after
    output += f'{word} - {count}\n'


# write the top ten words to a text file
# open new text file in WRITE mode ('w')
with open('most_frequent_words.txt', 'w') as text_file:
    # write the output string to the text file
    text_file.write(output)