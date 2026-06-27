#!/usr/bin/env python3
"""Quick test for benefits and payroll"""
import sys
sys.path.insert(0, 'c:/Users/bizle/OneDrive/bsean4890@gmail.com/four-era-env/OWLBAN-GROUP-NVIDIA')

from database_manager import DatabaseManager

db = DatabaseManager()
print("DB initialized")

# Test benefits
print("\n--- Testing add_employee_benefits ---")
try:
    result = db.add_employee_benefits(
        employee_id='TEST001',
        health_insurance_plan='Premium',
        health_insurance_provider='Blue Cross',
        health_insurance_premium=500.0,
        health_insurance_coverage_type='family'
    )
    print(f"Add Benefits: {result}")
except Exception as e:
    print(f"Benefits Error: {e}")

# Test payroll  
print("\n--- Testing process_payroll ---")
try:
    result = db.process_payroll(
        payroll_id='PYR-TEST001',
        employee_id='TEST001',
        pay_period_start='2024-01-01',
        pay_period_end='2024-01-15',
        pay_date='2024-01-15',
        base_salary=5000.0
    )
    print(f"Process Payroll: {result}")
except Exception as e:
    print(f"Payroll Error: {e}")

print("\nDONE")
