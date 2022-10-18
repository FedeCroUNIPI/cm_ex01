"""Useful functions for bookstat.py
"""

import string
import matplotlib.pyplot as plt
import numpy as np

def counter_letters(file_path):
    """Open a file and count letters"""
    print(f'Opening input file: {file_path}')
    with open(file_path,'r',encoding='utf-8') as book: #with: open and close file
        #To not differentiate uppercase/lowercase and count twice
        text=book.read().lower() #lower: uppercase to lowercase letters
        alphabet=dict.fromkeys(string.ascii_lowercase,0)
        for i in string.ascii_lowercase:
            counter=text.count(i)
            alphabet[i]=counter
        return alphabet

def counter_spaces(file_path):
    """Open a file and count spaces"""
    print(f'Opening input file: {file_path}')
    with open(file_path,'r',encoding='utf-8') as book:
        text=book.read().lower()
        count=0
        for j in text:
            if j == ' ':
                count+=1
        return count

def counter_words(file_path):
    """Open a file and count words"""
    print(f'Opening input file: {file_path}')
    with open(file_path,'r',encoding='utf-8') as book:
        text=book.read().lower()
        counts=dict()
        words=text.split()
        for j in words:
            if j in counts:
                counts[j]+=1
            else:
                counts[j]=1
        return counts

def make_histo(alphabet_freq):
    """Create a normalizetd histogram"""
    n_tot=0
    for i in alphabet_freq:
        n_tot+=alphabet_freq[i]
    for i in alphabet_freq:
        alphabet_freq[i]=alphabet_freq[i]*(100./n_tot)
    plt.bar(alphabet_freq.keys(),alphabet_freq.values())
    plt.title('Percentage histogram')
    plt.show()