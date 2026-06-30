#!/usr/bin/env python
"""Test database_manager.py syntax"""
import sys
try:
    import database_manager
    print("SUCCESS: database_manager.py imports without syntax errors")
    sys.exit(0)
except SyntaxError as e:
    print(f"SYNTAX ERROR: {e}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
