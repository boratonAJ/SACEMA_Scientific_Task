#!/usr/bin/python3
"""
Ajayi Olabode
April 25, 2019
This script count the words in the files and write their frequency in their respective files
"""

from sys import argv, exit
import sys, getopt
from collections import defaultdict, Counter

# Reads in text files and writes out word frequency data
# This python function will display the content of the file whose name you pass in the first argument like that:
def readFile_Freq(argv):
    for filename in argv[1:]:
        freq = defaultdict(int)
        freq = Counter()
        for line in open(filename, encoding='utf-8'):
            words = line.strip().lower().split(' ')
            for word in words:
                freq.update([''.join(char for char in word if char.isalnum())])
        del freq['']
        with open(filename[:-3]+'freq', 'w') as my_file:
            for word_ct in freq.most_common():
                my_file.write(word_ct[0] + ' ' + str(word_ct[1]) + '\n')
            for word in freq.items():
                if word[0] is not None:
                    print(word)
# Main function to run the above function and program
def main(argv):
    while True:
        try:
            inputfile = ''
            opts, args = getopt.getopt(argv,"hi:",["ifile="])
        except getopt.GetoptError:
            print ('usage: python3 wordfreq.py -i <inputfile>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print ('usage: python3 wordfreq.py -i <inputfile>')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
                print ('Input file is: "', inputfile)
        return readFile_Freq(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
