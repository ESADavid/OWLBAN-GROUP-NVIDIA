#!/usr/bin/env python3
"""Debug table schema"""
import sqlite3

conn = sqlite3.connect('owlban_ai.db')
cursor = conn.cursor()

# Get table schema
cursor.execute("PRAGMA table_info(employee_benefits)")
rows = cursor.fetchall()
print("Table columns:")
for row in rows:
    print(f"  {row[1]} ({row[2]})")
