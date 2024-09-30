#!/usr/bin/env python3

import sys

phone_book = {}

with open(sys.argv[1]) as f:
    for line in f:
        line = line.split()
        phone_book[line[0]] = (line[1], line[2])

for line in sys.stdin:
    line = line.strip()
    print(f'Name: {line}')
    try:
        print(f'Phone: {phone_book[line][0]}')
        print(f'Email: {phone_book[line][1]}')
    except KeyError:
        print('No such contact')
