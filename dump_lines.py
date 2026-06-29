#!/usr/bin/env python3
"""Dump lines"""

with open('database_manager.py', 'r') as f:
    lines = f.readlines()

# Find add_employee_benefits and dump lines 530-590
for i in range(525, min(600, len(lines))):
    print(i, lines[i], end='')
