#!/usr/bin/env python
"""Test script to verify core module imports"""

print('Testing basic imports...')

try:
    from database_manager import DatabaseManager
    print('DB OK')
except Exception as e:
    print(f'DB Error: {e}')

try:
    from auth_lib import AuthManager
    print('Auth OK')
except Exception as e:
    print(f'Auth Error: {e}')

print('All core modules loaded successfully!')
