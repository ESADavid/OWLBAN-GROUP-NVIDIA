#!/usr/bin/env python3
"""Show specific lines from auth_lib.py"""

with open('auth_lib.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show all lines with errors (based on diagnostics)
error_lines = [242, 273, 302, 312, 329, 352, 365, 372, 376, 390, 399, 410, 426, 454, 499, 514, 530, 547]
for line_num in error_lines:
    idx = line_num - 1
    # Show 3 lines before and after for context
    start = max(0, idx - 2)
    end = min(len(lines), idx + 3)
    print(f"\n--- Lines {start+1} to {end} (focus on {line_num}) ---")
    for i, line in enumerate(lines[start:end], start=start+1):
        marker = ">>>" if i == line_num else "   "
        print(f'{marker} {i}: |{line.rstrip()}|')
