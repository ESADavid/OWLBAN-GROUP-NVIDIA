#!/usr/bin/env python3
"""Script to read specific lines from auth_lib.py"""

with open('auth_lib.py', 'r') as f:
    lines = f.readlines()

# Print lines 120-145 (to see the try block issue)
for i in range(119, 145):  # 120 is index 119
    print(f'{i+1}: {lines[i]}', end='')
