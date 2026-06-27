#!/usr/bin/env python3
"""Debug test"""
import sys
sys.path.insert(0, '.')

import sqlite3

# Test the exact query
conn = sqlite3.connect('owlban_ai.db')
cursor = conn.cursor()

# Build the values tuple
employee_id = 'EMP999'
health_insurance_plan = 'Premium'
health_insurance_provider = 'Blue Cross'
health_insurance_premium = 500.0
health_insurance_coverage_type = 'family'
life_insurance_status = 'enrolled'
life_insurance_amount = 100000
life_insurance_provider = 'MetLife'
life_insurance_premium = 50.0
life_insurance_beneficiary = None
k401_enrolled = True
k401_contribution_percentage = 6.0
k401_employer_match_percentage = 4.0

values_tuple = (employee_id, health_insurance_plan, health_insurance_provider,
               health_insurance_premium, health_insurance_coverage_type,
               life_insurance_status, life_insurance_amount,
               life_insurance_provider, life_insurance_premium,
               life_insurance_beneficiary, 1 if k401_enrolled else 0,
               k401_contribution_percentage, k401_employer_match_percentage)

print(f'Number of values: {len(values_tuple)}')
print(f'Values: {values_tuple}')

# Count the columns in the query
cols = '(employee_id, health_insurance_plan, health_insurance_provider, health_insurance_premium, health_insurance_coverage_type, life_insurance_status, life_insurance_amount, life_insurance_provider, life_insurance_premium, life_insurance_beneficiary, k401_enrolled, k401_contribution_percentage, k401_employer_match_percentage)'
num_cols = cols.count(',') + 1
print(f'Number of columns: {num_cols}')

# Now try execute
try:
    sql = """INSERT OR REPLACE INTO employee_benefits 
               (employee_id, health_insurance_plan, health_insurance_provider, health_insurance_premium,
                health_insurance_coverage_type, life_insurance_status, life_insurance_amount, life_insurance_provider,
                life_insurance_premium, life_insurance_beneficiary, k401_enrolled, k401_contribution_percentage,
                k401_employer_match_percentage)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(sql, values_tuple)
    conn.commit()
    print('SUCCESS!')
except Exception as e:
    print(f'ERROR: {e}')

conn.close()
