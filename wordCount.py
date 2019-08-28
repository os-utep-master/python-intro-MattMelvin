"""
@author: mjmelvin
Created August  27, 2019
This program takes two text files, keeps track of the number of times each word occurs in the first file, and then
writes the words and their totals two the second file
"""

import re
import sys

word_count = {}
punctuation_pattern = r'[,.;:!?"]'
hyphen_pattern = r'[-]'

input_file = sys.argv[1]
output_file = sys.argv[2]

if __name__ == '__main__':
    with open(input_file) as f:
        text = f.read()
        text = re.sub(punctuation_pattern, '', text)
        text = re.sub(hyphen_pattern, ' ', text)
        text = text.lower()
        words = text.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_keys = sorted(word_count.keys())
    sorted_values = sorted(word_count.values())

    with open(output_file, 'w') as f:
        for key, value in zip(sorted_keys, sorted_values):
            f.write(key + ' ' + str(value) + '\n')
