from string import punctuation

def read_text_file(filename):
    '''Open a text file, read its contents and return them as a giant string'''
    with open('alice.txt', 'r') as text_file:
        # alice.txt is open ONLY in this code block
        
        # read the file's contents and save to a variable as a giant string
        contents = text_file.read()
    # text file is closed at this indentation level
    
    return contents

def scrub_text(dirty_text):
    '''Clean text by lowercasing everything, removing new line characters and punctuation
    and splitting at each space into a list of words. Return the list of words.'''
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

    # return list of lowercase words with no punctuation or new lines
    return word_list

def tally_words(word_list):
    '''Loop through the list of words and populate
    a dictionary with the words as keys and their
    occurances as values. Return the dictionary of counts'''
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

    return word_counts

def sort_by_value(tup):
    '''return the first item of the tuple for sorting'''
    return tup[1]

def find_most_frequent(word_counts, n):
    '''Return a dictionary of the top n most frequently ocurring 
    words in the word_counts dictionary.'''
    words = list(word_counts.items())

    # sort the list of tuple items by value in descending order
    words.sort(key=sort_by_value, reverse=True)

    # empty list for top n words
    top_n = [] # list slicing - words[0:n] # list_name[start_index:stop_index]

    # loop 0 - 9
    for index in range(n):
        # add each of the top ten words to the list
        top_n.append(words[index])

    top_n = dict(top_n)

    return top_n

def write_text_file(filename, top_n, n):
    '''Write contents as a string to the filename, 
    displaying top n words and their counts.'''
    # label for output
    output = f'Top {n} Words\n-------------\n'

    # number for labeling words
    word_num = 1
    
    # 'unpack' the word and count for each item into two variables
    for word, count in top_n.items():
        # add the current word and its count to the output string with a new line after
        output += f'{word_num}. {word} - {count}\n'

        # increment word number
        word_num += 1

    # open new text file in WRITE mode ('w')
    with open(filename, 'w') as text_file:
        # write the output string to the text file
        text_file.write(output) 

    return output
