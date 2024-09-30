#!/usr/bin/env python3

import sys

def is_prime(n):
	for i in range (2, int(n ** 0.5) + 1):
		if not n % i:
			return False
	return True


for line in sys.stdin:
	M = int(line.strip()) + 1
	primes = [n for n in range(2, M) if is_prime(n)]
	print(f'Primes: {primes}')