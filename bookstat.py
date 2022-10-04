#!/usr/bin/env python
# Copyright (C) 2022 f.crognale@studenti.unipi.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""1st assignment for the CMEPDA course, 2022/23.
"""

import argparse
import string
import time #elapsed time
import matplotlib.pyplot as plt
import numpy as np

def process(file_path):
    """Open a file and count letters"""
    print(f'Opening input file: {file_path}')
    #***It must skip preamble, .... : overstimated numbers of letters***
    with open(file_path,'r',encoding='utf-8') as book: #with: open and close file
        text=book.read().lower() #lower: uppercase to lowercase letters
        #To not differentiate uppercase/lowercase and count twice
        alphabet=dict.fromkeys(string.ascii_lowercase,0)
        for i in string.ascii_lowercase:
            counter=text.count(i)
            alphabet[i]=counter
        return alphabet

def make_histo(alphabet_freq):
    """Create a histogram"""
    #Total number of letters
    n_tot=0
    for i in alphabet_freq:
        n_tot+=alphabet_freq[i]
    #Normalization
    #for i in alphabet_freq:
        #alphabet_freq[i]=alphabet_freq[i]/n_tot
    plt.bar(alphabet_freq.keys(),alphabet_freq.values()) #x-axis, y-axis values
    plt.show()

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="Print some book statistics")
    parser.add_argument('input_file', type=str, help="path of input file") #help option
    args=parser.parse_args()
    start=time.time() #start for elapsed time
    frequency=process(args.input_file)
    end=time.time() #end for elapsed time
    make_histo(frequency)
    print('Totale elapsed time:',end-start)
