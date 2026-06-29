"""Check detailed lines in database_manager_fixed.py for debugging."""
with open('database_manager_fixed.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # Find the process_payroll method and print those lines
    in_method = False
    for i, line in enumerate(lines, start=1):
        if 'def process_payroll' in line:
            in_method = True
        if in_method:
            print(f'{i}: {repr(line)}')
            if 'cursor.execute' in line:
                # Print next 20 lines
                for j in range(20):
                    if i+j < len(lines):
                        print(f'{i+j+1}: {repr(lines[i+j])}')
                break
