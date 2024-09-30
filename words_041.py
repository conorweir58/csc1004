#!/usr/bin/env python3

import sys
import string
d = {}

words = sys.stdin.read().lower().strip()

for c in words:
    if c in string.punctuation and c != "'":
        words = words.replace(c, "")

words = words.split()

for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

d = sorted(d.items())
for word in d:
    print(f'{word[0]} : {word[1]}')
