#!/usr/bin/python3
"""
Python 3
Program Version: 1.0
Ajayi Olabode
April 25, 2019

Main function to run the words_frequency function

Reads in text files and writes out word frequency data
This python function will display the content of the file whose name you pass in the first argument like that:
"""
from sys import argv, exit
import getopt
from frequency_of_words import words_frequency
import sys

def main(argv):
    while True:
        try:
            inputfile = ''
            opts, args = getopt.getopt(argv,"hi:",["ifile="])
        except getopt.GetoptError:
            print ('usage: python3 script/wordfreq.py -i <Data/input_file/inputfile>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print ('usage: python3 script/wordfreq.py -i <Data/input_file/inputfile>')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
                print ('Input file is: "', inputfile)
        return words_frequency(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
