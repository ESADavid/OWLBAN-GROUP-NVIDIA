#!/usr/bin/env python3
"""Debug DB"""

import sys
sys.path.insert(0, '.')

# Clear database
import os
if os.path.exists('owlban_ai.db'):
    os.remove('owlban_ai.db')

from database_manager import DatabaseManager
import traceback

db = DatabaseManager()

# Count function parameters
import inspect
sig = inspect.signature(db.add_employee_benefits)
print("Function parameters:", len(sig.parameters))
print("Params:", list(sig.parameters.keys()))

# Manually call with debug
print("\n--- Calling add_employee_benefits ---")
try:
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
except Exception as e:
    print("Error:", e)
    traceback.print_exc()

print("\n--- Done ---")
