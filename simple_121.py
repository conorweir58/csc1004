#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    letters = set(line)
    print(letters)
    simplicity = len(letters)
    print(simplicity)
    counts = sorted([(line.count(c), c) for c in letters])
    print(counts)

    deletions = 0
    while 2 < simplicity:
        (n, c) = counts.pop(0)
        print((n, c))
        deletions += n
        simplicity -= 1

    print(deletions)
    print('---------------')