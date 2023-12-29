# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:31:32 2023

@author: CEO1
"""

# importing modules
import enchant
from itertools import permutations

# declaring global lists and variables
global Lists
Lists = []
global ans
ans = []
global times
global Liste
Liste = [] 
global all_words 
all_words = enchant.Dict("en_US")

    
# returns the created words/letters from the function "possible" without the tuples
def lixt(func):
    def inner(*args, **kwargs):
        returned_value = func(*args, **kwargs)
        for i in returned_value:
            st = ''.join(map(str, i))
            Liste.append(st)
        del Liste[0]  # optional
        return Liste
    return inner


# function that provide all possible combinations of the letters in "entry"
@lixt
def possible(entry:str, word:int) -> list:
    global add_to
    add_to = 0
    while add_to <= word:
        global words
        words = permutations(entry, add_to)
        add_to += 1
        for i in words:
            Lists.append(i)
    return Lists


def filtering(Liste):
    for i in Liste:
        k = bool(all_words.check(i))
        if k:
            if len(i) == 1:
                pass
            elif len(i)==2:
                pass
            else:
                ans.append(i)
    s = set(ans)
    return s


# Runner Code
if __name__ == "__main__":
    entry = str(input("ENTER THE WORD: "))
    word = len(entry)
    possible(entry, word)
    print(f"Possible words from that can be formed from {entry} are: ")
    print(filtering(Liste))
    

""" happy coding """
    