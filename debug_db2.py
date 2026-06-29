#!/usr/bin/env python3
"""Debug DB more"""

import sys
import os
sys.path.insert(0, '.')

# Clear database
if os.path.exists('owlban_ai.db'):
    os.remove('owlban_ai.db')

# Import and patch to see values
import database_manager

original_add_benefits = database_manager.DatabaseManager.add_employee_benefits

def patched_add_employee_benefits(self, employee_id: str, health_insurance_plan=None,
                             health_insurance_provider=None,
                             health_insurance_start_date=None,
                             health_insurance_premium=None,
                             health_insurance_coverage_type=None,
                             life_insurance_status="not_enrolled",
                             life_insurance_amount=None,
                             life_insurance_provider=None,
                             life_insurance_premium=None,
                             life_insurance_beneficiary=None,
                             k401_enrolled=False,
                             k401_contribution_percentage=None,
                             k401_employer_match_percentage=None,
                             k401_start_date=None,
                             k401_current_balance=None,
                             benefits_notes=None):
    
    values = (employee_id, health_insurance_plan, health_insurance_provider, health_insurance_start_date,
              health_insurance_premium, health_insurance_coverage_type, life_insurance_status,
              life_insurance_amount, health_insurance_provider, life_insurance_premium,
              life_insurance_beneficiary, 1 if k401_enrolled else 0,
              k401_contribution_percentage, k401_employer_match_percentage,
              k401_start_date, k401_current_balance, benefits_notes)
    
    print(f"TOTAL values being passed: {len(values)}")
    for i, v in enumerate(values):
        print(f"  [{i}] = {repr(v)}")
    
    return original_add_benefits(self, employee_id, health_insurance_plan,
                             health_insurance_provider,
                             health_insurance_start_date,
                             health_insurance_premium,
                             health_insurance_coverage_type,
                             life_insurance_status,
                             life_insurance_amount,
                             life_insurance_provider,
                             life_insurance_premium,
                             life_insurance_beneficiary,
                             k401_enrolled,
                             k401_contribution_percentage,
                             k401_employer_match_percentage,
                             k401_start_date,
                             k401_current_balance,
                             benefits_notes)

database_manager.DatabaseManager.add_employee_benefits = patched_add_employee_benefits

from database_manager import DatabaseManager

db = DatabaseManager()

print("\n--- Calling ---\n")
result = db.add_employee_benefits(
    employee_id='EMP001',
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
print("Result:", result)
