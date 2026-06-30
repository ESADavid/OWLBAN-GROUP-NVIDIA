# Pylint Diagnostics Fix Plan for auth_lib.py

## Information Gathered

Analyzed `auth_lib.py` (~600 lines) and identified the following Pylint warnings:

### Warning Categories

1. **W0718: broad-exception-caught** (4 occurrences)
   - Lines 134, 142, 151, 163
   - Catching generic `Exception` in try-except blocks

2. **W0621: redefined-outer-name** (16 occurrences)
   - Variables like `user`, `message`, `access_token`, `refresh_token`, `payload` being redefined in functions
   - Happens when iterating with `for user in self.users.values()` while `User` is a class

3. **W0613: unused-argument** (2 occurrences)
   - Lines 243, 244: `ip_address`, `user_agent` in `authenticate_user`

4. **C0116: missing-function-docstring** (6 occurrences)
   - Lines 43, 52, 567, 570, 573, 577 - Functions missing docstrings

5. **C0301: line-too-long** (multiple)
   - Lines exceeding 100 character limit

6. **C0209: consider-using-f-string** (multiple)
   - Old-style string formatting should be f-strings

7. **C0303: trailing-whitespace** (multiple)
   - Trailing whitespace on several lines

## Fix Plan

### Step 1: Fix Broad Exception Handling

Replace generic `except Exception` with specific exceptions:

- `json.JSONDecodeError` for JSON parsing
- `IOError` / `OSError` for file operations
- `jwt.InvalidTokenError` for JWT issues

### Step 2: Fix Redefined Outer Names

Rename loop variables to avoid conflicts:

- Change `for user in self.users.values()` to `for user_obj in self.users.values()`
- Change `message` to `msg` or similar
- Change `payload` to `token_payload`

### Step 3: Fix Unused Arguments

Either use the arguments or prefix with underscore to indicate intentionally unused:

- `_ip_address`, `_user_agent`

### Step 4: Add Missing Docstrings

Add docstrings to functions at lines 43, 52, 567, 570, 573, 577

### Step 5: Fix Line Too Long

Break long lines at appropriate points

### Step 6: Convert to F-Strings

Replace `% formatting` with f-strings

### Step 7: Remove Trailing Whitespace

Strip trailing whitespace

## Dependent Files

None - directly editing auth_lib.py

## Followup Steps

1. Run pylint to verify fixes
2. Test authentication functionality
