#!/usr/bin/env python3

import sys

correct_chess = [2, 2, 4, 4, 4, 16]

for line in sys.stdin:
    changes = []
    check_chess = [int(n) for n in line.strip().split()]
    for i in range(len(check_chess)):
        changes.append(str(correct_chess[i] - check_chess[i]))
    print(' '.join(changes))
