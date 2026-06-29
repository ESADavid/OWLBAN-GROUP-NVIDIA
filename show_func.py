#!/usr/bin/env python3
"""Extract function for debugging"""

with open('database_manager.py', 'r') as f:
    content = f.read()

# Find add_employee_benefits function
start = content.find('def add_employee_benefits')
if start != -1:
    # Find next function
    next_func = content.find('\n    def ', start + 1)
    if next_func == -1:
        next_func = content.find('\n    # ===', start + 1)
    print("=== add_employee_benefits ===")
    print(content[start:next_func])
    print("\n=== process_payroll ===")
    start2 = content.find('def process_payroll')
    if start2 != -1:
        next_func2 = content.find('\n    def ', start2 + 1)
        if next_func2 == -1:
            next_func2 = content.find('\n    # ===', start2 + 1)
        print(content[start2:next_func2])
