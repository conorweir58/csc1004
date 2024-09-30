#!/usr/bin/env python3
 
import sys

def length_17(dic):
    length_17 = [line for line in dic if len(line) == 17]
    return(length_17)

def length_18plus(dic):
    length_18plus = [line for line in dic if len(line) >= 18]
    return(length_18plus)

def four_a(dic):
    four_a = []
    for line in dic:
        no_a = line.lower().count('a')
        if no_a == 4:
            four_a.append(line)
    return(four_a)

def two_plus_q(dic):
    two_plus_q = []
    for line in dic:
        no_q = line.lower().count('q')
        if no_q >= 2:
            two_plus_q.append(line)
    return(two_plus_q)

def contains_cie(dic):
    contains_cie = [line for line in dic if 'cie' in line]
    return(contains_cie)

def anagram(dic):
    check = 'angle'
    anagram = []
    for line in dic:
        word1 = line.lower()
        i = 0
        while i < len(check) and check[i] in word1 and word1 != check:
            word1 = word1.replace(check[i], ' ', 1)
            i += 1
        
        if word1 == (' ' * len(check)) and i == len(check):
            anagram.append(line)
        
    return(anagram)


dic = sys.stdin.read().split()

print("Words containing 17 letters:",length_17(dic))
print("Words containing 18+ letters:",length_18plus(dic))
print("Words with 4 a's:", four_a(dic))
print("Words with 2+ q's:", two_plus_q(dic))
print("Words containing cie:", contains_cie(dic))
print("Anagrams of angle:", anagram(dic))