#!/usr/bin/env python3

import sys

punctuation = '.,!?;:\n'
words = []

for line in sys.stdin:
    censored_txt = []
    line = line.split()
    for word in line:

        org = word
        check = word
        if word[-1] in punctuation:
            check = word[:-1]

        if check.lower() not in words:

            words.append(check.lower())
            censored_txt.append(org)

        else:
            censored_txt.append('.')

    print(' '.join(censored_txt))