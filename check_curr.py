#!/usr/bin/env python3
with open('auth_lib.py', 'r') as f:
    lines = f.readlines()
for i in range(118, 150):
    print(f'{i+1}: {lines[i]}', end='')
