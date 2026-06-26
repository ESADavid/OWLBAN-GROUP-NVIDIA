import sys
sys.path.insert(0, r'c:\Users\bizle\OneDrive\bsean4890@gmail.com\four-era-env\OWLBAN-GROUP-NVIDIA')

with open(r'c:\Users\bizle\OneDrive\bsean4890@gmail.com\four-era-env\OWLBAN-GROUP-NVIDIA\database_manager.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section
start = content.find('INSERT OR REPLACE INTO employee_benefits')
if start >= 0:
    # Get the SQL part
    sql_part = content[start:start+500]
    
    # Count ? in the VALUES part
    values_start = sql_part.find('VALUES')
    if values_start >= 0:
        values_part = sql_part[values_start:sql_part.find(')', values_start)]
        print("=== VALUES part ===")
        print(repr(values_part))
        print("=== Placeholder count ===")
        print(values_part.count('?'))
        
    # Print the full SQL part
    print("=== Full SQL ===")
    print(sql_part[:300])
