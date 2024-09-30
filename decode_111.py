#!/usr/bin/env python3

import sys

vowels = 'aeiou'

for line in sys.stdin:
    line = line.strip()
    i = 0
    while i < len(line) - 1:
        if line[i] in vowels:
            line = line[:i] + line[i+2:]
        i += 1

    print(line)
