#!/usr/bin/env python3

import sys

line = sys.stdin.read().split()
d = {}
letters = line.pop(-1)

i = 0
while i < len(line):
    line[i] = int(line[i])
    i += 1

line.sort()

d['A'] = line[0]
d['B'] = line[1]
d['C'] = line[2]

print(d[letters[0]], d[letters[1]], d[letters[2]])
