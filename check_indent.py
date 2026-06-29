#!/usr/bin/env python3
"""Check indentation in auth_lib.py"""

with open('auth_lib.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[220:330], start=221):
    if line.strip():
        indent = len(line) - len(line.lstrip())
        display_indent = indent // 4
        print(f'{i:3d} [{display_indent:2d}]: {line.rstrip()}')
