#!/usr/bin/env python3

import sys

steps = int(sys.stdin.readline().strip())

jumps = sys.stdin.readline().strip().split()
jumps = [int(k) for k in jumps]

count = 0

for k in jumps:
	tmp = steps
	while 0 < tmp:
		tmp = tmp - k

	if tmp == 0:
		count += 1

if sum(jumps) == steps:
	count += 2
elif steps % sum(jumps) == 0:
	count = 2 * (3 * (steps / sum(jumps)))

print(int(count))