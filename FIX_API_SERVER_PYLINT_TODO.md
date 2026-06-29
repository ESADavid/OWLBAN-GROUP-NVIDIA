# Fix api_server.py Pylint Warnings - TODO

## Priority 1: High Impact Fixes (Critical)

### 1.1 Unused Arguments (W0613) - Lines 58-75

**Issue**: Fallback auth functions have unused parameters
**Fix**: Add `_` prefix to unused parameters in fallback functions

- Line 58: `email` → `_email`
- Line 59: `password` → `_password`  
- Line 60: `ip_address` → `_ip_address`
- Line 61: `user_agent` → `_user_agent`
- Line 66: `email` → `_email`
- Line 67: `username` → `_username`
- Line 68: `password` → `_password`
- Line 69: `role` → `_role`
- Line 70: `company` → `_company`
- Line 71: `permissions` → `_permissions`
- Line 75: `token` → `_token`

### 1.2 Broad Exception Caught (W0718) - Multiple Lines

**Issue**: Catching too general exception Exception
**Fix**: Replace with specific exceptions

- Lines 180, 189, 196, 203: Use `HTTPException` or `ValueError`
- Lines 351, 394, 430, 494, 519: Use appropriate specific exceptions
- Lines 689, 721, 743, 768, 821, 861: Use `HTTPException` or `ValueError`
- Lines 893, 917, 948, 1011, 1026, 1043: Use specific exceptions

### 1.3 Raise Missing From (W0707) - Line 475

**Issue**: Need to explicitly re-raise with `from e`
**Fix**: Add `from e` to raise statement

## Priority 2: Important Fixes

### 2.1 Missing Docstrings (C0115, C0116)

**Issue**: Missing function/class docstrings
**Fix**: Add docstrings to:

- Line 57: `register_user` function
- Line 65: `login_user` function
- Line 75: `refresh_token_endpoint` function
- Lines 207, 211, 215, 226, 237, 247, 262, 281, 291, 299, 303, 310, 313, 316: All model classes
- Line 528: `get_logs` function
- Line 532: `add_log_entry` function
- Line 536: `get_metrics` function
- Line 572, 589, 601, 613, 625, 637, 649: Various endpoints

### 2.2 Trailing Whitespace (C0303)

**Issue**: Trailing whitespace on lines
**Fix**: Remove trailing whitespace from lines 64, 74, 680, 711, 736, 759, 907

### 2.3 Line Too Long (C0301)

**Issue**: Lines exceeding 100 characters
**Fix**: Break long lines at:

- Lines 554, 555: 104, 107 chars
- Lines 672-675: 119, 123, 124, 119 chars
- Line 945, 946: 147, 142 chars
- Line 1114: 128 chars
- Line 1177: 107 chars

### 2.4 Import Outside Toplevel (C0415)

**Issue**: Imports inside function bodies
**Fix**: Move imports to top-level or add condition to suppress

### 2.5 Unused Import (W0611) - Line 871

**Issue**: `AdvancedAnomalyDetection` imported but unused
**Fix**: Add `_` prefix or remove import

### 2.6 Unused Variable (W0612) - Line 780

**Issue**: `detector` variable unused
**Fix**: Use the variable or remove it

### 2.7 Global Statement (W0603) - Line 172

**Issue**: Using global statement
**Fix**: Refactor to avoid global or suppress warning

### 2.8 Redefined Outer Name (W0621)

**Issue**: `status` redefined at lines 1177, 1360
**Fix**: Rename local variable to avoid conflict

## Priority 3: Code Style Improvements

### 3.1 Ungrouped Imports (C0412)

**Fix**: Group imports properly

### 3.2 Consider Using F-string (C0209)

**Fix**: Convert to f-string at line 581

### 3.3 Too Many Lines (C0302)

**Note**: This is a module-level issue that may require splitting the file

## Files to Edit

- `api_server.py`

## Follow-up Steps

1. Run pylint to verify fixes
2. Test API endpoints to ensure functionality is intact
