#!/usr/bin/env python3
"""Dump lines"""

with open('database_manager.py', 'r') as f:
    lines = f.readlines()

# Find add_employee_benefits and dump lines 600-700
for i in range(600, min(720, len(lines))):
    print(i, lines[i], end='')
