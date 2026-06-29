#!/usr/bin/env python3
with open('auth_lib.py', 'r') as f:
    lines = f.readlines()
for i in range(124, 140):
    print(f'{i+1}: {lines[i]}', end='')
