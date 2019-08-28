"""
@author: mjmelvin
Created August  27, 2019
This program takes two text files, keeps track of the number of times each word occurs in the first file, and then
writes the words and their totals two the second file
"""

import re   # punctuation and hyphen removal
import sys  # command line arguments

# variable initialization
word_count = {}

# regex patterns to remove punctuation and hyphen
punctuation_pattern = r'[,.;:!?"]'
hyphen_pattern = r'[-]'

# get files from command line
input_file = sys.argv[1]
output_file = sys.argv[2]

if __name__ == '__main__':
    # open file and store text
    with open(input_file) as f:
        text = f.read()

    # transform text into list of single words
    text = text.lower()
    text = re.sub(punctuation_pattern, '', text)
    text = re.sub(hyphen_pattern, ' ', text)
    words = text.split()

    # count occurrences of word in list
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # store keys and value in separate sorted list
    sorted_keys = sorted(word_count.keys())

    # write keys and values to file in required format
    with open(output_file, 'w') as f:
        for key in sorted_keys:
            f.write(key + ' ' + str(word_count[key]) + '\n')
