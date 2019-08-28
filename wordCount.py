"""
@author: mjmelvin
Created August  27, 2019
This program takes two text files, keeps track of the number of times each word occurs in the first file, and then
writes the words and their totals two the second file
"""

import re
import sys

dictionary = {}
pattern = r'[,.;:!?"]'

input_file = sys.argv[1]
output_file = sys.argv[2]

if __name__ == '__main__':
    with open(input_file) as f:
        text = f.read()
        text = re.sub(pattern, '', text)
        text = text.lower()
        words = text.split()

    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    sorted_keys = sorted(dictionary.keys())
    sorted_values = sorted(dictionary.values())
