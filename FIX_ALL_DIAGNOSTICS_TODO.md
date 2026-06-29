# Fix All Diagnostics TODO

## Issues Found

### auth_lib.py Issues (Priority: High)
1. [ ] Line 33: `created_at: datetime = None` - Type error: Should be `Optional[datetime] = None`
2. [ ] Line 199: `permissions: List[str] = None` - Should be `permissions: Optional[List[str]] = None`
3. [ ] Line 429-435: PasswordResetToken instantiation - Incorrect field order in dataclass
4. [ ] Line 516: Same permissions default issue
5. [ ] Line 9: Remove unused import hashlib
6. [ ] Lines 124, 132, 141, 153: Catch specific exceptions instead of broad Exception
7. [ ] Lines211, 218, 236, etc.: Rename variables to avoid shadowing outer scope
8. [ ] Lines233, 234: Add underscore prefix to unused args (ip_address, user_agent)
9. [ ] Lines8-15: Fix import order (standard imports first, then third-party)
10. [ ] Lines43, 52: Add missing function docstrings
11. [ ] Lines104, 174, 185, etc.: Fix line lengths (split long lines)
12. [ ] Multiple: Convert to f-strings where applicable
13. [ ] Lines428, 438, 442, 480, 487: Remove trailing whitespace
14. [ ] Lines509, 512, 515, 519: Add missing function docstrings
15. [ ] PEP 484: Fix implicit Optional (use Optional[] explicitly)

### database_manager_clean.py Issues (Priority: Critical)
1. [ ] Line 83: Fix indentation (syntax error - unindent doesn't match)
2. [ ] Lines14, 15: Add optional handling for pymongo import

### debug_db2.py Issues (Priority: Medium)
1. [ ] Line 45: Too many arguments for method call
2. [ ] Lines13, 64: Move imports to top

## Plan

### Phase 1: Fix Critical Syntax Errors
- [ ] Fix database_manager_clean.py indentation

### Phase 2: Fix Type Errors in auth_lib.py
- [ ] Fix Optional type hints

### Phase 3: Fix Import Issues
- [ ] Remove unused imports in auth_lib.py
- [ ] Fix import order in auth_lib.py
- [ ] Move imports to top in debug_db2.py

### Phase 4: Fix Style Issues
- [ ] Fix line lengths
- [ ] Add f-strings
- [ ] Remove trailing whitespace
- [ ] Add docstrings

### Phase 5: Fix Exception Handling
- [ ] Catch specific exceptions

## Dependencies
- Need to modify: auth_lib.py, database_manager_clean.py, debug_db2.py
