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
    line = line.split()
    team = ' '.join(line[1:-8])
    curr = len(team.rstrip())
    long = longest(long, curr)
    long = long

print(f'{"OS" : <{4}}{"CLUB" : <{long}}{"P" : >{3}}{"W" : >{4}}{"D" : >{4}}{"L" : >{4}}{"GF" : >{4}}{"GA" : >{4}}{"GD" : >{4}}{"PTS" : >{4}}')

for line in text:
    line = line.split()
    print(f'{line[0] : >{3}}{" "}{" ".join(line[1:-8]) : <{long}}{line[-8] : >{3}}{line[-7] : >{4}}{line[-6] : >{4}}{line[-5] : >{4}}{line[-4] : >{4}}{line[-3] : >{4}}{line[-2] : >{4}}{line[-1] : >{4}}')
