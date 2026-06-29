#!/usr/bin/env python3
"""Script to read specific lines from auth_lib.py - reset_password and convenience functions"""

with open('auth_lib.py', 'r') as f:
    lines = f.readlines()

# Print lines 450-480 (reset_password function)
print("=== Lines 450-480 (reset_password function) ===")
for i in range(449, 480):
    print(f'{i+1}: {lines[i]}', end='')

print("\n\n=== Lines 555-580 (convenience functions) ===")
# Print lines 555-580
for i in range(554, 580):
    print(f'{i+1}: {lines[i]}', end='')
