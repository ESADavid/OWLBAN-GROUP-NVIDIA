#!/usr/bin/env python3
"""Check indentation in auth_lib.py"""

with open('auth_lib.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check lines 330-560
for i, line in enumerate(lines[330:560], start=331):
    if line.strip():
        indent = len(line) - len(line.lstrip())
        display_indent = indent // 4
        print(f'{i:3d} [{display_indent:2d}]: {line.rstrip()}')
