from utilities import (
    read_text_file, 
    scrub_text, 
    tally_words, 
    find_most_frequent, 
    write_text_file
)

def main():
    # open a text file
    dirty_text = read_text_file('alice.txt')

    # clean the text and create list of words
    word_list = scrub_text(dirty_text)

    # loop through the list of words and count the number of occurances of each
    word_counts = tally_words(word_list)
    
    # number of words to show
    n = 15

    # find the top n most frequent words and their counts
    top_n = find_most_frequent(word_counts, n)
    

    # write the top n words to a text file
    print(write_text_file('top_n_words.txt', top_n, n))

main()