"""Check lines 780-790 in database_manager_fixed.py for debugging."""
with open('database_manager_fixed.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines[780:790], start=781):
        print(f'Line {i}: {len(line)} chars')
        print(f'Content: {repr(line[:100])}...')
        print()
