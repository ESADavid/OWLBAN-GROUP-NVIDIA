#!/usr/bin/env python3
"""
Add Three Employees: Oscar Broome, David Leeper, Sandra Edwards
Complete employee setup: database, benefits, payroll, and authentication
"""
# pylint: disable=wrong-import-position
# pylint: disable=import-outside-toplevel
# pylint: disable=logging-fstring-interpolation

import sys
sys.path.insert(0, 'c:/Users/bizle/OneDrive/bsean4890@gmail.com/four-era-env/OWLBAN-GROUP-NVIDIA')

import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def add_employees_to_database():
    """Add all three employees to the database"""
    from database_manager import DatabaseManager

    db = DatabaseManager()

    # Define employees data
    employees = [
        {
            "employee_id": "OSCAR001",
            "first_name": "Oscar",
            "last_name": "Broome",
            "email": "oscar.broome@owlban.com",
            "phone": "555-0101",
            "position": "CEO",
            "department": "Executive",
            "salary": 250000.00,
            "hire_date": "2024-01-01"
        },
        {
            "employee_id": "DAVID002",
            "first_name": "David",
            "last_name": "Leeper",
            "email": "david.leepr@owlban.com",
            "phone": "555-0102",
            "position": "Chief Technology Officer",
            "department": "Technology",
            "salary": 200000.00,
            "hire_date": "2024-01-15"
        },
        {
            "employee_id": "SANDRA03",
            "first_name": "Sandra",
            "last_name": "Edwards",
            "email": "sandra.edwards@owlban.com",
            "phone": "555-0103",
            "position": "Chief Financial Officer",
            "department": "Finance",
            "salary": 200000.00,
            "hire_date": "2024-02-01"
        }
    ]

    success_count = 0
    for emp in employees:
        result = db.add_employee(**emp)
        if result:
            logger.info("Added employee: %s - %s %s",
                      emp['employee_id'], emp['first_name'], emp['last_name'])
            success_count += 1
        else:
            logger.error("Failed to add employee: %s", emp['employee_id'])

    return success_count


def add_employee_benefits():
    """Add benefits for all three employees"""
    from database_manager import DatabaseManager

    db = DatabaseManager()

    # Define benefits data (only parameters accepted by the database_manager)
    benefits = [
        {
            "employee_id": "OSCAR001",
            "health_insurance_plan": "Premium",
            "health_insurance_provider": "Blue Cross",
            "health_insurance_premium": 750.00,
            "health_insurance_coverage_type": "family",
            "life_insurance_status": "enrolled",
            "life_insurance_amount": 500000,
            "life_insurance_provider": "MetLife",
            "life_insurance_premium": 100.00,
            "life_insurance_beneficiary": "Jane Broome",
            "k401_enrolled": True,
            "k401_contribution_percentage": 10.0,
            "k401_employer_match_percentage": 6.0
        },
        {
            "employee_id": "DAVID002",
            "health_insurance_plan": "Premium",
            "health_insurance_provider": "Blue Cross",
            "health_insurance_premium": 650.00,
            "health_insurance_coverage_type": "family",
            "life_insurance_status": "enrolled",
            "life_insurance_amount": 300000,
            "life_insurance_provider": "MetLife",
            "life_insurance_premium": 75.00,
            "life_insurance_beneficiary": "Mary Leeper",
            "k401_enrolled": True,
            "k401_contribution_percentage": 8.0,
            "k401_employer_match_percentage": 5.0
        },
        {
            "employee_id": "SANDRA03",
            "health_insurance_plan": "Standard",
            "health_insurance_provider": "Aetna",
            "health_insurance_premium": 450.00,
            "health_insurance_coverage_type": "single",
            "life_insurance_status": "enrolled",
            "life_insurance_amount": 200000,
            "life_insurance_provider": "MetLife",
            "life_insurance_premium": 50.00,
            "life_insurance_beneficiary": "Thomas Edwards",
            "k401_enrolled": True,
            "k401_contribution_percentage": 6.0,
            "k401_employer_match_percentage": 4.0
        }
    ]

    success_count = 0
    for ben in benefits:
        employee_id = ben["employee_id"]
        result = db.add_employee_benefits(**ben)
        if result:
            logger.info("Added benefits for: %s", employee_id)
            success_count += 1
        else:
            logger.error("Failed to add benefits for: %s", employee_id)

    return success_count


def add_payroll_records():
    """Add payroll records for all three employees"""
    from database_manager import DatabaseManager

    db = DatabaseManager()

    # Get today's date for calculations
    today = datetime.now()
    pay_period_start = today.replace(day=1).strftime("%Y-%m-%d")
    pay_period_end = today.strftime("%Y-%m-%d")
    pay_date = today.strftime("%Y-%m-%d")

    # Define payroll data (bi-weekly base salary)
    payrolls = [
        {
            "payroll_id": "PYR-OSCAR-001",
            "employee_id": "OSCAR001",
            "pay_period_start": pay_period_start,
            "pay_period_end": pay_period_end,
            "pay_date": pay_date,
            "base_salary": 9615.38,  # ~250k/year / 26 pay periods
            "overtime_pay": 0,
            "bonuses": 0,
            "commissions": 0,
            "federal_tax_rate": 0.24,
            "state_tax_rate": 0.05,
            "social_security_rate": 0.062,
            "medicare_rate": 0.0145,
            "health_insurance_premium": 0,
            "life_insurance_premium": 0,
            "k401_contribution": 961.54,
            "other_deductions": 0,
            "payment_method": "direct_deposit"
        },
        {
            "payroll_id": "PYR-DAVID-001",
            "employee_id": "DAVID002",
            "pay_period_start": pay_period_start,
            "pay_period_end": pay_period_end,
            "pay_date": pay_date,
            "base_salary": 7692.31,  # ~200k/year / 26 pay periods
            "overtime_pay": 0,
            "bonuses": 0,
            "commissions": 0,
            "federal_tax_rate": 0.22,
            "state_tax_rate": 0.05,
            "social_security_rate": 0.062,
            "medicare_rate": 0.0145,
            "health_insurance_premium": 0,
            "life_insurance_premium": 0,
            "k401_contribution": 615.38,
            "other_deductions": 0,
            "payment_method": "direct_deposit"
        },
        {
            "payroll_id": "PYR-SANDRA-001",
            "employee_id": "SANDRA03",
            "pay_period_start": pay_period_start,
            "pay_period_end": pay_period_end,
            "pay_date": pay_date,
            "base_salary": 7692.31,  # ~200k/year / 26 pay periods
            "overtime_pay": 0,
            "bonuses": 0,
            "commissions": 0,
            "federal_tax_rate": 0.22,
            "state_tax_rate": 0.05,
            "social_security_rate": 0.062,
            "medicare_rate": 0.0145,
            "health_insurance_premium": 0,
            "life_insurance_premium": 0,
            "k401_contribution": 461.54,
            "other_deductions": 0,
            "payment_method": "direct_deposit"
        }
    ]

    success_count = 0
    for pyr in payrolls:
        result = db.process_payroll(**pyr)
        if result:
            # pylint: disable=logging-fstring-interpolation
            logger.info("Processed payroll for: %s - Net: $%.2f",
                       pyr['employee_id'], result['net_pay'])
            success_count += 1
        else:
            logger.error("Failed to process payroll for: %s", pyr['employee_id'])

    return success_count


def add_auth_users():
    """Add user accounts for authentication"""
    from auth_lib import create_user

    # Define users (username, password, role, permissions)
    users = [
        {
            "email": "oscar.broome@owlban.com",
            "username": "oscar_broome",
            "password": "Oscar2024!",
            "role": "executive",
            "company": "OSCAR_BROOME",
            "permissions": ["read", "write", "admin", "manage_users"]
        },
        {
            "email": "david.leepr@owlban.com",
            "username": "david_leeper",
            "password": "David2024!",
            "role": "executive",
            "company": "OWLBAN_GROUP",
            "permissions": ["read", "write", "admin", "manage_users"]
        },
        {
            "email": "sandra.edwards@owlban.com",
            "username": "sandra_edwards",
            "password": "Sandra2024!",
            "role": "executive",
            "company": "OWLBAN_GROUP",
            "permissions": ["read", "write", "admin", "manage_finance"]
        }
    ]

    success_count = 0
    for user in users:
        success, message = create_user(
            email=user["email"],
            username=user["username"],
            password=user["password"],
            role=user["role"],
            company=user["company"],
            permissions=user["permissions"]
        )
        if success:
            logger.info("Created user account: %s", user["email"])
            success_count += 1
        else:
            # User might already exist, try to authenticate
            logger.info("User may already exist: %s - %s", user["email"], message)

    return success_count


def verify_employees():
    """Verify all employees are in the database"""
    from database_manager import DatabaseManager

    db = DatabaseManager()

    employee_ids = ["OSCAR001", "DAVID002", "SANDRA03"]

    logger.info("=" * 60)
    logger.info("VERIFICATION: Employee Records")
    logger.info("=" * 60)

    for emp_id in employee_ids:
        emp = db.get_employee(emp_id)
        if emp:
            logger.info("Verified %s: %s %s - %s",
                      emp_id, emp['first_name'], emp['last_name'], emp['position'])
            # Get benefits
            ben = db.get_employee_benefits(emp_id)
            if ben:
                logger.info("  Benefits: Health=%s, 401k=%s",
                            ben['health_insurance_plan'], ben['k401_enrolled'])
        else:
            logger.error("Not found: %s", emp_id)

    return True


def main():
    """Main function to add all three employees"""
    logger.info("%s", "=" * 60)
    logger.info("%s", "ADDING EMPLOYEES: Oscar Broome, David Leeper, Sandra Edwards")
    logger.info("%s", "=" * 60)

    results = {}

    # 1. Add employees to database
    logger.info("\n[1/5] Adding employees to database...")
    results['employees'] = add_employees_to_database()
    logger.info("Added %d employees", results['employees'])

    # 2. Add employee benefits
    logger.info("\n[2/5] Adding employee benefits...")
    results['benefits'] = add_employee_benefits()
    logger.info("Added benefits for %d employees", results['benefits'])

    # 3. Add payroll records
    logger.info("\n[3/5] Processing payroll...")
    results['payroll'] = add_payroll_records()
    logger.info("Processed payroll for %d employees", results['payroll'])

    # 4. Add authentication users
    logger.info("\n[4/5] Creating user accounts...")
    results['auth_users'] = add_auth_users()
    logger.info("Created %d user accounts", results['auth_users'])

    # 5. Verify employees
    logger.info("\n[5/5] Verifying employees...")
    results['verified'] = verify_employees()

    # Summary
    logger.info("\n%s", "=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)
    logger.info("Employees Added: %d/3", results.get('employees', 0))
    logger.info("Benefits Added: %d/3", results.get('benefits', 0))
    logger.info("Payroll Processed: %d/3", results.get('payroll', 0))
    logger.info("User Accounts: %d/3", results.get('auth_users', 0))
    logger.info("=" * 60)
    logger.info("EMPLOYEE SETUP COMPLETE")

    return results


if __name__ == "__main__":
    main()
