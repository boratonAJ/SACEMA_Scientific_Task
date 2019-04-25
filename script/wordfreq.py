#!/usr/bin/python3
"""
Ajayi Olabode
April 25, 2019
This script count the word frequency
"""

from sys import argv, exit
from collections import defaultdict, Counter

# Reads in text files and writes out word frequency data

if len(argv) == 1:
    print('\n\tUsage:\t./wordfreq.py *.txt\n')
    exit()

#for filename in argv[1:]:
    #freq = defaultdict(int)
    #for line in open(filename, encoding='utf-8'):
        #words = line.strip().lower().split(' ')
        #for word in words:
            #freq[''.join(char for char in word if char.isalnum())] += 1
    #for word_ct in freq.most_common():
        #print(word_ct[0], word_ct[1])
    #for word in sorted(freq.items(), key=freq.get, reverse=True):
        #print(word, freq[word])
    #for word_count in sorted(freq.items(), key=lambda kv: kv[1])
    #print(freq)

for filename in argv[1:]:
    #freq = defaultdict(int)
    freq = Counter()
    for line in open(filename, encoding='utf-8'):
        words = line.strip().lower().split(' ')
        for word in words:
            freq.update([''.join(char for char in word if char.isalnum())])
            #freq[''.join(char for char in word if char.isalnum())] += 1
    del freq['']
    fo = open(filename[:-3]+'freq', 'w')
    for word_ct in freq.most_common():
        fo.write(word_ct[0] + ' ' + str(word_ct[1]) + '\n')
        #print(word_ct[0], word_ct[1])
    #for word in sorted(freq.items(), key=freq.get, reverse=True):
        #print(word, freq[word])
    fo.close()
