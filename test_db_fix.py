#!/usr/bin/env python
"""Test database manager syntax and imports."""
import sys
try:
    from database_manager import DatabaseManager
    print("Database manager imports OK")
    
    # Test instantiation
    db = DatabaseManager()
    print("Database manager instantiated OK")
    
    # Test add_employee_benefits method signature
    import inspect
    sig = inspect.signature(db.add_employee_benefits)
    params = list(sig.parameters.keys())
    print(f"add_employee_benefits params: {params}")
    
    # Check for required new parameters
    expected_params = ['employee_id', 'health_insurance_plan', 'health_insurance_provider',
                      'health_insurance_start_date', 'health_insurance_premium',
                      'health_insurance_coverage_type', 'life_insurance_status', 'life_insurance_amount',
                      'life_insurance_provider', 'life_insurance_premium', 'life_insurance_beneficiary',
                      'k401_enrolled', 'k401_contribution_percentage', 'k401_employer_match_percentage',
                      'k401_start_date', 'k401_current_balance', 'benefits_notes']
    
    for p in expected_params:
        if p in params:
            print(f"  {p}: OK")
        else:
            print(f"  {p}: MISSING")
            sys.exit(1)
    
    print("\nAll tests passed!")
    db.close_all()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
