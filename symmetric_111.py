#!/usr/bin/env python3

import sys

output = []

for line in sys.stdin:
    line = line.strip()
    middle = (len(output) // 2)
    output.insert(middle, line)

output = output[::-1]
for line in output:
    print(line)
