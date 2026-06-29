#!/usr/bin/env python3
"""Check current lines around 128-135"""

with open('auth_lib.py', 'r') as f:
    lines = f.readlines()

for i in range(126, 145):
    print(f'{i+1}: {lines[i]}', end='')
