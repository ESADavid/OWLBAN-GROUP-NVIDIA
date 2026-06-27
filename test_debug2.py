#!/usr/bin/env python3
"""Debug test - exact method simulation"""
import sqlite3

# Build the values EXACTLY like add_employee_benefits does
employee_id = 'EMP999'
health_insurance_plan = 'Premium'
health_insurance_provider = 'Blue Cross'
health_insurance_premium = 500.0
health_insurance_coverage_type = 'family'
life_insurance_status = 'enrolled'
life_insurance_amount = 100000
life_insurance_provider = 'MetLife'  # Different value after first provider
life_insurance_premium = 50.0
life_insurance_beneficiary = None
k401_enrolled = True
k401_contribution_percentage = 6.0
k401_employer_match_percentage = 4.0

# Build tuple exactly like method
values_tuple = (employee_id, health_insurance_plan, health_insurance_provider,
               health_insurance_premium, health_insurance_coverage_type,
               life_insurance_status, life_insurance_amount,
               life_insurance_provider, life_insurance_premium,
               life_insurance_beneficiary, 1 if k401_enrolled else 0,
               k401_contribution_percentage, k401_employer_match_percentage)

print(f'Values: {values_tuple}')
print(f'Count: {len(values_tuple)}')

# Check for duplicates in the tuple
unique = set()
dupes = []
for i, v in enumerate(values_tuple):
    if v in unique:
        dupes.append((i, v))
    unique.add(v)
if dupes:
    print(f'Duplicates: {dupes}')
