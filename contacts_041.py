#!/usr/bin/env python3

import sys

phone_book = {}

with open(sys.argv[1]) as f:
    for line in f:
        line = line.split()
        phone_book[line[0]] = line[1]

for line in sys.stdin:
    line = line.strip()
    print(f'Name: {line}')
    try:
        print(f'Phone: {phone_book[line]}')
    except KeyError:
        print('No such contact')
