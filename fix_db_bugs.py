#!/usr/bin/env python3
"""
Fix bugs in database_manager.py:
1. add_employee_benefits: 14 columns but 13 values (extra updated_at in SQL)
2. process_payroll: 21 columns but 20 values (missing payroll_id in VALUES)
"""
import re

def fix_bugs():
    with open('database_manager.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
# Bug 1 Fix: Remove updated_at from SQL in add_employee_benefits
    old_benefits_sql = '''cursor.execute(
                """INSERT OR REPLACE INTO employee_benefits
                   (employee_id, health_insurance_plan, health_insurance_provider, health_insurance_premium,
                    health_insurance_coverage_type, life_insurance_status, life_insurance_amount, life_insurance_provider,
                    life_insurance_premium, life_insurance_beneficiary, k401_enrolled, k401_contribution_percentage,
                    k401_employer_match_percentage, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)""",'''
    
    new_benefits_sql = '''cursor.execute(
                """INSERT OR REPLACE INTO employee_benefits 
                   (employee_id, health_insurance_plan, health_insurance_provider, health_insurance_premium,
                    health_insurance_coverage_type, life_insurance_status, life_insurance_amount, life_insurance_provider,
                    life_insurance_premium, life_insurance_beneficiary, k401_enrolled, k401_contribution_percentage,
                    k401_employer_match_percentage)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",'''
    
    if old_benefits_sql in content:
        content = content.replace(old_benefits_sql, new_benefits_sql)
        print("Fixed Bug 1: add_employee_benefits - removed extra updated_at column")
    else:
        print("Bug 1: Pattern not found")
    
    # Bug 2 Fix: Add payroll_id to VALUES in process_payroll
    old_payroll_sql = '''cursor.execute(
                """INSERT INTO payroll 
                   (payroll_id, employee_id, pay_period_start, pay_period_end, pay_date, base_salary,
                    overtime_pay, bonuses, commissions, federal_tax_withholding, state_tax_withholding,
                    social_security_tax, medicare_tax, health_insurance_premium, life_insurance_premium,
                    k401_contribution, other_deductions, gross_pay, net_pay, payment_status, payment_method)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?)""",'''
    
    new_payroll_sql = '''cursor.execute(
                """INSERT INTO payroll 
                   (payroll_id, employee_id, pay_period_start, pay_period_end, pay_date, base_salary,
                    overtime_pay, bonuses, commissions, federal_tax_withholding, state_tax_withholding,
                    social_security_tax, medicare_tax, health_insurance_premium, life_insurance_premium,
                    k401_contribution, other_deductions, gross_pay, net_pay, payment_status, payment_method)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?)""",'''
    
    if old_payroll_sql in content:
        content = content.replace(old_payroll_sql, new_payroll_sql)
        print("Fixed Bug 2: process_payroll - added payroll_id to VALUES")
    else:
        print("Bug 2: Pattern not found")
    
    with open('database_manager.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Done!")

if __name__ == "__main__":
    fix_bugs()
