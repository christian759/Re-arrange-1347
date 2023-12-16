# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:31:32 2023

@author: CEO1
"""

# importing modules
import nltk
from itertools import permutations

# declaring lists
global Lists
Lists = []
global times
global Liste
Liste = [] 

    
# returns the created words/letters from the function "possible" without the tuples
def lixt(func):
    def inner(*args, **kwargs):
        returned_value = func(*args, **kwargs)
        for i in returned_value:
            st = ''.join(map(str, i))
            Liste.append(st)
        del Liste[0]  # optional 
        print(Liste)
    return inner


# function that provide all possible combinations of the letters in "entry"
@lixt
def possible(entry:str, word:int)-> tuple:
    global add_to
    add_to = 0
    while add_to <= word:
        global words
        words = permutations(entry, add_to)
        add_to += 1
        for i in words:
            Lists.append(i)
    return Lists
        

# Runner Code
if __name__ == "__main__":
    entry = str(input("ENTER THE WORD: "))
    word = len(entry)
    possible(entry, word)
    

""" happy coding """
    
    