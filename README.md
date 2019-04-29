## Word Frequency Counter Program

This repo contain solution to an assessment exercise for assessing technical skills and experience that are required for the position of Junior Researcher – Scientific Programming at the DST-NRF Centre of Excellence in Epidemiological Modelling and Analysis.


### Installation

#### External dependencies

`SACEMA_Scientific_Task` depends on the following programs and libraries:

* [Python](https://www.python.org/downloads/release/python-373/) (version 3.7.3) 
* [Collections](https://docs.python.org/2/library/collections.html)
* [Python Documentation](https://docs.python.org/2/contents.html) 
* New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.


## Getting Started

### Description


SACEMA_Scientific_Task is a Python script program that allows you to count the frequency usage of each word in text. 

The main script reads a text file and computes the frequency of words that appear in the text file.

Its features include:

* Python module function a getopt that helps you parse command-line options and arguments.
* Libraries dependency calculation and checkpointing.

 
#### Important Notes:

The current script is designed to work with text file


### Inputs & Outputs

##### Supporting Input format

* .txt - Plain text file.`

##### Output format

* .freq - A plain text file with extension `.freq`

#### Input Data, Scripts and File Location:

File Folder for input and output do you want to search:

* `SACEMA_Scientific_Task` 			- current project folder (SACEMA_Scientific_Task).
* `cd script/` 					- go to script folder (the folder contain `frequency_of_words.py` and `main_function.py`).
* `cd Data/` 					- go to data folder to view the file input and output file folder.
* `cd Doc/`					- document folder 

### Usage: How to execute the script

Code explanation is located in the comments:



```
`cd script/`

usage: python3 main_function.py [-h] [-i, --ifile, [inputfile]]

Example: python3 main_function.py Data/input_file/*.txt

```


### Unit test and Test cases


We used Python Unit test to checks if some specific parts of the function’s behaviour are correct. This make integrating the functions together with main parts much easier. 

##### Please Note that: 

Test case is a collection of unit tests which together proves that a function works as intended, inside a full range of situations in which that function may find itself and that it’s expected to handle. 

Test case should consider all possible kinds of input a function could receive from users, and therefore should include tests to represent each of these situations.


### License

GNU GENERAL PUBLIC LICENSE. See LICENSE.txt in source repository.



### References:

1. [SEAMS Workshop](https://seams-workshop.gitlab.io/practical/workspace/)



































