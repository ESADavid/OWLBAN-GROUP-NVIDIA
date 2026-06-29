#!/usr/bin/env python3
"""Script to read specific lines from auth_lib.py"""

with open('auth_lib.py', 'r') as f:
    lines = f.readlines()

# Print lines 183-210 (adjusting for 0-based index)
for i in range(182, 210):  # 183 is index 182
    print(f'{i+1}: {lines[i]}', end='')
