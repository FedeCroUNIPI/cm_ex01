"""
    Analyze a book

    For the moment there is not the option about skip preamble
"""

#Import packages
import argparse
from argparse import RawTextHelpFormatter #for formatting help
import time #elapsed time
import matplotlib.pyplot as plt
import numpy as np

import my_functions as my #my personal functions

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="Print some book statistics", formatter_class=RawTextHelpFormatter)
    parser.add_argument('input_file', metavar='File', type=str, help="path of input file") #help option
    parser.add_argument('choice_stat', metavar='Choice', type=str, help='type of statistics\n'
    '0 - all letters\n'
    '0_histo - all letters with histogram\n'
    'a,b,c,... - choose from alphabet\n'
    'word - number of words\n'
    'space - number of spaces')
    args=parser.parse_args()

    #Rename for semplicity
    choice=args.choice_stat
    infile=args.input_file

    t_start=time.time() #start for elapsed time
    
    #What to do
    if choice == '0':
        frequency=my.counter_letters(infile)
        for i in frequency:
            print(f'{i}\t{frequency[i]}')
    elif choice == '0_histo':
        frequency=my.counter_letters(infile)
        for i in frequency:
            print(f'{i}\t{frequency[i]}')
        t_end=time.time() #end for elapsed time
        #Here time elapsed time because histo does not stop running time
        print(f'Total elapsed time: {t_end-t_start}')
        my.make_histo(frequency)
    elif choice == 'word':
        word_result=my.counter_words(infile)
        print(f'Total number of words: {len(word_result)}')
    elif choice == 'space':
        space_result=my.counter_spaces(infile)
        print(f'Number of spaces: {space_result}')
    else:
        frequency=my.counter_letters(infile)
        print(f'{choice}\t{frequency[choice]}')
    
    #Compute the elapsed time
    if choice != '0_histo':
        t_end=time.time() #end for elapsed time
        print(f'Totale elapsed time: {t_end-t_start}')
