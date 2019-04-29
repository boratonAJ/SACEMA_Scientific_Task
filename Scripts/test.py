import unittest
from main_function import *
from frequency_of_words import words_frequency
import time

class checkingfrequencyWordsTestCase(unittest.TestCase):

    def test_remove_first_space_from_tel(self):
        result = words_frequency("Data/input_file/11-0.txt")
        self.assertEqual(result, "11-0.txt")
        print("Passed")
