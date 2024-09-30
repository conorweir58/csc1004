#!/usr/bin/env python3

import sys

def swap_keys_values(my_dict):
    d = {}
    for k, v in my_dict.items():
        d[v] = k
    return d