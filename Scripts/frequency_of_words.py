#!/usr/bin/python3
"""
Python 3
Program Version: 1.0
Ajayi Olabode
April 25, 2019

A Python script that compute the frequency of the words from the input (text file). The script count the words in the files
and write their frequency in their respective files. The output is after sorting the key alphanumerically.

"""
import collections
import operator

def words_frequency(argv):
    for filename in argv[1:]:
        freq = collections.Counter()
        for line in open(filename, encoding='utf-8'):
            words = line.strip().lower().split(' ')
            for word in words:
                freq.update([''.join(char for char in word if char.isalnum())])
        del freq['']
        output_filename = 'Data/output/' + filename.split("/")[2][:-3] +'freq' #  substring the filename (slicing)
        with open(output_filename, 'w') as my_file:
            for word_ct in freq.most_common():
                my_file.write(word_ct[0] + ' ' + str(word_ct[1]) + '\n') # write (word_ct[0], word_ct[1]) to file
            for word in sorted(freq.items(), key=operator.itemgetter(1), reverse=True): #Sort by dict value - descending
                print("{0}:{1}".format(word[0], word[1]))
