# Database Fix TODO

## Issues Identified:

1. **database_manager_clean.py** - Syntax error at line 80 (missing except/finally block)
2. **Employee Benefits** - Column mismatch in INSERT statement
3. **Payroll** - Column mismatch in INSERT statement
4. **database_manager.py** - Indentation issues

## Fix Plan:

### Step 1: Fix database_manager.py indentation issues
- Fix `# Quantum computations` comment indentation at line ~120
- Fix `# Save to MongoDB if available` comment indentation

### Step 2: Fix add_employee_benefits() method
- Add missing columns: k401_start_date, k401_current_balance
- 14 placeholders + 2 = 16 placeholders + CURRENT_TIMESTAMP

### Step 3: Fix process_payroll() method
- Add missing columns to match table schema
- 21 values expected, need to add columns

### Step 4: Test the fixes
- Run test_simple.py to verify

## Execution:
- [ ] 1. Fix database_manager.py indentation
- [ ] 2. Fix add_employee_benefits INSERT columns  
- [ ] 3. Fix process_payroll INSERT columns
- [ ] 4. Run test to verify
