#!/usr/bin/env python3

import sys

correct_text = sys.stdin.readline().strip().split()
sticky_text = sys.stdin.readline().strip().split()

sticky_letters = set()

for i in range(len(correct_text)):
    
    for c in correct_text[i]:

        if c in sticky_text[i]:
            tmp = sticky_text[i].index(c)
            sticky_text[i] = sticky_text[i][:tmp] + sticky_text[i][tmp + 1:]
        
letters = ''.join(sticky_text)

for c in letters:

    sticky_letters.add(c)

print(''.join(sorted(sticky_letters)))
