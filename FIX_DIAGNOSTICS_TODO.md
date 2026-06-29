# FIX ALL DIAGNOSTICS TODO

## Information Gathered

Analyzed diagnostics from test_oscar_auth.py and auth_lib.py. Issues identified:

### test_oscar_auth.py (1 issue)

- Line 85: f-string without interpolation

### auth_lib.py (50+ issues)

- Mypy: permissions default None vs list[str] (lines 199, 516)
- Mypy: PasswordResetToken unexpected keyword args (line 429)
- Pylint: Unused import hashlib (line 9)
- Pylint: Broad exception caught (lines 124, 132, 141, 153)
- Pylint: Redefined outer names (multiple lines)
- Pylint: Unused arguments ip_address, user_agent (lines 233-234)
- Pylint: Wrong import order (lines 8-15)
- Pylint: Missing function docstrings (multiple)
- Pylint: Line too long (multiple)
- Pylint: Trailing whitespace (multiple)
- Pylint: Consider using f-strings (multiple)

## Plan

### Phase 1: Fix test_oscar_auth.py

- [ ] 1. Fix f-string on line 85 (remove f prefix)

### Phase 2: Fix auth_lib.py Import Order

- [ ] 2. Reorder imports: standard, then third-party (lines 8-15)

### Phase 3: Fix Mypy Type Errors

- [ ] 3. Fix permissions default: None -> []
- [ ] 4. Fix PasswordResetToken class field order

### Phase 4: Fix Pylint Issues

- [ ] 5. Remove unused hashlib import
- [ ] 6. Add docstrings to functions
- [ ] 7. Fix long lines (wrap or shorten)
- [ ] 8. Fix trailing whitespace
- [ ] 9. Use f-strings consistently
- [ ] 10. Fix broad exception handling
- [ ] 11. Fix redefined outer names (rename local vars)
- [ ] 12. Fix unused arguments (add underscore prefix)

## Dependent Files

- test_oscar_auth.py (direct fix)
- auth_lib.py (direct fix)

## Followup Steps

- Run pylint and mypy to verify fixes
- Check for any new warnings introduced
