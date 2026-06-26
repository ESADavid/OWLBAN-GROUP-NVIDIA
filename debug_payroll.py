#!/usr/bin/env python3
"""Debug script to find exact column/value mismatch"""
import sqlite3

conn = sqlite3.connect('owlban_ai.db')
c = conn.cursor()

# Get benefits table column names
c.execute("PRAGMA table_info(employee_benefits)")
cols = [row[1] for row in c.fetchall()]
print("Benefits columns:", cols)
print("Count:", len(cols))

# Remove first and last (id + timestamps)
custom_cols = cols[1:-2]  # Skip id, created_at, updated_at
print("Custom columns:", custom_cols)
print("Custom count:", len(custom_cols))

# Create insert with exact count
vals = ('DEBUG001', 'Premium', 'BlueCross', '2024-01-01', 500.0, 'family', 'enrolled', 50000.0, 'MetLife', 25.0, 'Spouse', 1, 6.0, 4.0, '2024-01-01', 0.0, 'Active')  # 17 values

qmarks = '?, ' * len(vals)
qmarks = qmarks[:-2]

sql = f"INSERT OR REPLACE INTO employee_benefits ({', '.join(custom_cols)}) VALUES ({qmarks})"
print("SQL:", sql)
print("Placeholders:", sql.count('?'))
print("Values:", len(vals))

try:
    c.execute("DELETE FROM employee_benefits WHERE employee_id = 'DEBUG001'")
    c.execute(sql, vals)
    conn.commit()
    print("SUCCESS!")
except Exception as e:
    print("ERROR:", e)

conn.close()
