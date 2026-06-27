#!/usr/bin/env python3
"""Fix the employee benefits column/values mismatch"""

with open('database_manager.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Current (broken): 14 placeholders but only 13 columns
# Fix: Change 14 ? to 13 ?
old = 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
new = 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

if old in content:
    content = content.replace(old, new)
    print('Fixed: removed extra placeholder')
    with open('database_manager.py', 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print('Pattern not found - checking current state')
    # Show what's there
    idx = content.find('INSERT OR REPLACE INTO employee_benefits')
    if idx >= 0:
        print(repr(content[idx:idx+300]))
