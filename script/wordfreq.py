#!/usr/bin/python3
"""
Ajayi Olabode
April 25, 2019
This script count the word frequency
"""

from sys import argv, exit
from collections import defaultdict, Counter

# Reads in text files and writes out word frequency data

import sys, getopt

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print ('python3 wordfreq.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print ('python3 wordfreq.py -i <inputfile>')
           sys.exit()
       elif opt in ("-i", "--ifile"):
           inputfile = arg
           print ('Input file is: "', inputfile)
   # This python function will display the content of the file whose name you pass in the first argument like that:
   for filename in argv[1:]:
        freq = defaultdict(int)
        freq = Counter()
        for line in open(filename, encoding='utf-8'):
            words = line.strip().lower().split(' ')
            #print (words)
            for word in words:
                freq.update([''.join(char for char in word if char.isalnum())])
                #freq[''.join(char for char in word if char.isalnum())] += 1
        #print(freq)
        #del freq['']
        #fo = open(filename[:-3]+'freq', 'w')

        with open(filename[:-3]+'freq', 'w') as my_file:
            print(my_file)
        #     for word_ct in freq.most_common():
        #         #my_file.write(word_ct[0] + ' ' + str(word_ct[1]) + '\n')
        #         print(word_ct[0], word_ct[1])
        # #for word in sorted(freq.items(), key=freq.get, reverse=True):
        #     #print(word, freq[word])
        # #fo.close()


if __name__ == "__main__":
   main(sys.argv[1:])


#
#
# if len(argv) == 1:
#     print('\n\tUsage:\t./wordfreq.py *.txt\n')
#     exit()
#
# #for filename in argv[1:]:
#     #freq = defaultdict(int)
#     #for line in open(filename, encoding='utf-8'):
#         #words = line.strip().lower().split(' ')
#         #for word in words:
#             #freq[''.join(char for char in word if char.isalnum())] += 1
#     #for word_ct in freq.most_common():
#         #print(word_ct[0], word_ct[1])
#     #for word in sorted(freq.items(), key=freq.get, reverse=True):
#         #print(word, freq[word])
#     #for word_count in sorted(freq.items(), key=lambda kv: kv[1])
#     #print(freq)
#
