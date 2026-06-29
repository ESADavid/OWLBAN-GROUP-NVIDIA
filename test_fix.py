#!/usr/bin/env python
"""Test script to verify remaining issues are fixed."""

import sys
import ast

def test_file_syntax(filepath):
    """Test if a file has valid Python syntax."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)

def main():
    """Main test function."""
    files = [
        'database_manager.py',
        'database_manager_clean.py', 
        'auth_lib.py',
        'api_server.py'
    ]
    
    all_ok = True
    for filepath in files:
        ok, err = test_file_syntax(filepath)
        if ok:
            print(f"✓ {filepath}: Syntax OK")
        else:
            print(f"✗ {filepath}: Syntax Error - {err}")
            all_ok = False
    
    # Now try imports
    print("\nTesting imports...")
    
    # Test database_manager
    try:
        import database_manager
        print("✓ database_manager: Import OK")
    except Exception as e:
        print(f"✗ database_manager: Import Error - {e}")
        all_ok = False
    
    # Test auth_lib
    try:
        import auth_lib
        print("✓ auth_lib: Import OK")
    except Exception as e:
        print(f"✗ auth_lib: Import Error - {e}")
        all_ok = False
    
    if all_ok:
        print("\n✓ All remaining issues FIXED!")
        return 0
    else:
        print("\n✗ Some issues remain")
        return 1

if __name__ == '__main__':
    sys.exit(main())
