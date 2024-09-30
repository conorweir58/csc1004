#!/usr/bin/env python3

import sys

words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

for line in sys.stdin:
        line = line.strip().split()
        nums2words = []
        for c in line:
                if int(c) <= 10:
                    nums2words.append(words[int(c)])
                else:
                    nums2words.append('unknown')
        print(' '.join(nums2words))

