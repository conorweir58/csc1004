#!/usr/bin/env python3

import sys

def longest (long, curr):
    '''Return longest line value'''
    if long < curr:
        long = curr
    return long

text = sys.stdin.readlines()
long = 0

for line in text:
    curr = len(line)
    long = longest(long, curr)

for line in text:
    line = line.rstrip()
    print(f'{line: ^{long - 1}}')
