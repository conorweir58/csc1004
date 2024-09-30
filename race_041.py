#!/usr/bin/env python3

import sys

def check_time(name, times):
    for word in times:
        word = word.replace(":", "")
        try:
            word = int(word)
            pass
        except ValueError:
            del(runs[name])
            pass

def mins_to_secs(str):
     divider = str.rfind(':')
     mins = str[:divider]
     secs = str[divider + 1:]
     try:
         mins_as_secs = int(mins) * 60
         total = mins_as_secs + int(secs)
         return total
     except ValueError:
         pass

runs = {}

for line in sys.stdin:
    line = line.strip().split()
    name = line[0]
    times = sorted(line[1:])
    runs[name] = sorted(times)
    check_time(name, times)

shortest = 0
for k, v in runs.items():
    best_time = mins_to_secs(v[0])
    if shortest == 0:
        shortest = best_time
        fastest = k
    elif best_time < shortest:
        shortest = best_time
        fastest = k

print(f"{fastest} : {runs[fastest][0]}")