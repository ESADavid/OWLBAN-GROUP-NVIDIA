#!/usr/bin/env python3
"""Test password reset functionality"""
import sys
sys.path.insert(0, '.')

from auth_lib import auth_manager

# Test password reset request
email = 'admin@owlban.com'
success, message = auth_manager.request_password_reset(email)
print(f'Request reset: success={success}, message={message}')

# Get the token from the stored tokens
if auth_manager.password_reset_tokens:
    for token, token_obj in list(auth_manager.password_reset_tokens.items())[:1]:
        print(f'Token generated: {token[:20]}...')
        
        # Test password reset confirm
        success2, msg2 = auth_manager.reset_password(email, token, 'NewPass123!')
        print(f'Confirm reset: success={success2}, message={msg2}')
else:
    print('No tokens found')

print('\nPassword reset test completed!')
