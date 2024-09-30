#!/usr/bin/env python3

import sys

letters = 'ABCDEF'
strnumbers = sys.stdin.readline().strip().split()
order = sys.stdin.readline().strip()

numbers = [int(c) for c in strnumbers]
numbers = sorted(numbers)

d = {k : v for k,v in zip(letters, numbers)}

output = (str(d[c]) for c in order)
print(' '.join(output))
