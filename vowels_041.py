#!/usr/bin/env python3

import sys

vowel_count = {}

txt = sys.stdin.read().lower().strip()

def count_vowel(c):
    '''Counts number of given vowel and adds it to a dictionary'''
    count = txt.count(c)
    vowel_count[c] = count
    return vowel_count

def tagger(item):
    return item[1]

count_vowel('a')
count_vowel('e')
count_vowel('i')
count_vowel('o')
count_vowel('u')

format = 0
for k, v in sorted(vowel_count.items(), key=tagger, reverse = True):
    if format == 0:
        format = len(str(v))
    print(f'{k} : {v : >{format}}')
