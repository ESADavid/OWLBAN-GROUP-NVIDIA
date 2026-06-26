#!/usr/bin/env python3
"""Test database employee operations"""

import sys
sys.path.insert(0, 'c:/Users/bizle/OneDrive/bsean4890@gmail.com/four-era-env/OWLBAN-GROUP-NVIDIA')

from database_manager import DatabaseManager

def test_employee_operations():
    # Initialize database
    db = DatabaseManager()
    print('Database Status:', db.get_database_status())
    
    # Test adding an employee
    result = db.add_employee(
        employee_id='EMP001',
        first_name='John',
        last_name='Doe',
        email='john.doe@owlban.com',
        phone='555-0100',
        position='Software Engineer',
        department='Engineering',
        salary=100000.0,
        hire_date='2024-01-15'
    )
    print('Add Employee:', result)
    
    # Get employee
    employee = db.get_employee('EMP001')
    print('Get Employee:', employee)
    
    # Add benefits
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
    print('Add Benefits:', result)
    
    # Process payroll
    payroll_result = db.process_payroll(
        payroll_id='PYR-001',
        employee_id='EMP001',
        pay_period_start='2024-01-01',
        pay_period_end='2024-01-15',
        pay_date='2024-01-15',
        base_salary=5000.0
    )
    print('Process Payroll:', payroll_result)
    
    print('All operations completed successfully!')

if __name__ == '__main__':
    test_employee_operations()
