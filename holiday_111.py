#!/usr/bin/env python3

import sys

temps = sys.stdin.read().strip().split()

grouped = []

i = 0
while i < len(temps) - 2:
   grouped.append((int(temps[i]), int(temps[i+2])))
   i += 1

highest = []
for group in grouped:
   highest.append(int(max(group)))

day = highest.index(min(highest)) + 1

print(int(day), int(min(highest)))