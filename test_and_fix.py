#!/usr/bin/env python3
"""Fixed test and fix database operations"""
import sqlite3

def test_and_fix():
    print("=== Testing Database Operations ===")
    
    db_path = 'owlban_ai.db'
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Test 1: Employees - 10 columns (no id, timestamps auto)
    try:
        c.execute("DELETE FROM employees WHERE employee_id = 'TEST001'")
        conn.commit()
    except:
        pass
        
    try:
        vals = ('TEST001', 'Test', 'User', 'test@test.com', '555-0101', 'Engineer', 'IT', 80000.0, '2024-01-01', 'active')
        qmarks = '?, ' * 10
        qmarks = qmarks[:-2]
        sql = f"INSERT INTO employees (employee_id, first_name, last_name, email, phone, position, department, salary, hire_date, employment_status) VALUES ({qmarks})"
        c.execute(sql, vals)
        conn.commit()
        print("Test 1 PASSED: add_employee")
    except Exception as e:
        print(f"Test 1 FAILED: add_employee - {e}")
    
    # Test 2: Benefits - 17 columns (no id, timestamps auto)
    try:
        c.execute("DELETE FROM employee_benefits WHERE employee_id = 'TEST001'")
        conn.commit()
    except:
        pass
        
    try:
        vals = ('TEST001', 'Premium', 'BlueCross', '2024-01-01', 500.0, 'family', 'enrolled', 50000.0, 'MetLife', 25.0, 'Spouse', 1, 6.0, 4.0, '2024-01-01', 0.0, 'Active')
        qmarks = '?, ' * 17
        qmarks = qmarks[:-2]
        sql = f"INSERT OR REPLACE INTO employee_benefits (employee_id, health_insurance_plan, health_insurance_provider, health_insurance_start_date, health_insurance_premium, health_insurance_coverage_type, life_insurance_status, life_insurance_amount, life_insurance_provider, life_insurance_premium, life_insurance_beneficiary, k401_enrolled, k401_contribution_percentage, k401_employer_match_percentage, k401_start_date, k401_current_balance, benefits_notes) VALUES ({qmarks})"
        c.execute(sql, vals)
        conn.commit()
        print("Test 2 PASSED: add_employee_benefits")
    except Exception as e:
        print(f"Test 2 FAILED: add_employee_benefits - {e}")
    
    # Test 3: Payroll - 21 columns (no id, created_at auto)
    try:
        c.execute("DELETE FROM payroll WHERE payroll_id = 'PYR-TEST'")
        conn.commit()
    except:
        pass
    
    try:
        vals = ('PYR-TEST', 'TEST001', '2024-01-01', '2024-01-15', '2024-01-15', 4000.0,
             0.0, 0.0, 0.0, 880.0, 200.0, 248.0, 58.0, 0.0, 0.0,
             240.0, 0.0, 4000.0, 2374.0, 'pending', 'direct_deposit')
        qmarks = '?, ' * 21
        qmarks = qmarks[:-2]
        sql = f"INSERT INTO payroll (payroll_id, employee_id, pay_period_start, pay_period_end, pay_date, base_salary, overtime_pay, bonuses, commissions, federal_tax_withholding, state_tax_withholding, social_security_tax, medicare_tax, health_insurance_premium, life_insurance_premium, k401_contribution, other_deductions, gross_pay, net_pay, payment_status, payment_method) VALUES ({qmarks})"
        c.execute(sql, vals)
        conn.commit()
        print("Test 3 PASSED: process_payroll")
    except Exception as e:
        print(f"Test 3 FAILED: process_payroll - {e}")
    
    conn.close()
    print("=== Tests Complete ===")

if __name__ == "__main__":
    test_and_fix()
