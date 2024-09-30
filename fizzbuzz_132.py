#!/usr/bin/env python3

import sys

numbers = sys.stdin.readline().strip().split()

x,y,n = [int(m) for m in numbers]

for i in range(n):
    i += 1
    if not((i % x)) and not((i % y)):
        print('fizzbuzz')
    elif not((i % x)):
        print('fizz')
    elif not((i % y)):
        print('buzz')
    else:
        print(i)