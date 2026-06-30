# auth_lib.py Pylint Fix TODO

## Task Summary

Fix all Pylint diagnostic warnings in auth_lib.py

## Issues to Fix

### 1. W0718: Broad exception caught (2 instances)

- Line 151: `except Exception`
- Line 163: `except Exception`
- Fix: Use more specific exceptions (json.JSONDecodeError, IOError, OSError)

### 2. W0621: Redefined outer name (multiple instances)

- Line 221: Redefining 'message'
- Line 228, 246, 274, 320, 330, 379, 403, 429, 483: Redefining 'user'
- Line 298: Redefining 'access_token'
- Line 299, 313: Redefining 'refresh_token'
- Line 306, 316: Redefining 'payload'
- Fix: Rename local variables to avoid shadowing outer scope names

### 3. W0613: Unused argument (2 instances)

- Line 243: Unused 'ip_address'
- Line 244: Unused 'user_agent'
- Fix: Use underscore prefix or use the arguments

### 4. C0116: Missing function docstring (4 instances)

- Line 43, 52: Missing function docstrings
- Lines 567, 570, 573, 577: Missing function docstrings at end of file
- Fix: Add docstrings to functions

### 5. C0301: Line too long (multiple instances)

- Fix: Break lines longer than 100 characters

### 6. C0209: Consider using f-string (multiple instances)

- Fix: Convert % formatting to f-strings

### 7. C0303: Trailing whitespace (multiple instances)

- Lines 438, 446, 448, 452, 490, 497
- Fix: Remove trailing whitespace

## Progress

- [ ] Fix W0718 broad exception warnings
- [ ] Fix W0621 redefined outer name warnings  
- [ ] Fix W0613 unused argument warnings
- [ ] Fix C0116 missing docstring warnings
- [ ] Fix C0301 line-too-long warnings
- [ ] Fix C0209 f-string warnings
- [ ] Fix C0303 trailing whitespace warnings
