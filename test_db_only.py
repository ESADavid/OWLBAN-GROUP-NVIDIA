#!/usr/bin/env python3
"""Minimal database test"""
import sys
sys.path.insert(0, '.')

# Test database only
from database_manager import DatabaseManager
db = DatabaseManager()
print("DB created")
status = db.get_database_status()
print(f"Status: {status}")

# Add test employee
db.add_employee("EMP001", "John", "Doe", "john@test.com", position="Engineer", salary=100000)
print("Employee added")

emp = db.get_employee("EMP001")
print(f"Employee: {emp}")

print("DB TEST DONE")
