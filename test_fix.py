#!/usr/bin/env python3
"""Test fix"""
import sys
sys.path.insert(0, '.')
from database_manager import DatabaseManager

db = DatabaseManager()
result = db.add_employee_benefits(
    employee_id='EMP999',
    health_insurance_plan='Premium',
    health_insurance_provider='Blue Cross',
    health_insurance_premium=500.0,
    health_insurance_coverage_type='family',
    life_insurance_status='enrolled',
    life_insurance_amount=100000,
    life_insurance_provider='MetLife',
    life_insurance_premium=50.0,
    k401_enrolled=True,
    k401_contribution_percentage=6.0,
    k401_employer_match_percentage=4.0
)
print('Result:', result)
