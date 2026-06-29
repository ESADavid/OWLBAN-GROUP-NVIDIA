# Fix Database Diagnostics TODO

## Task: Fix all diagnostics in database_manager_fixed.py

### Issues to Fix

1. **pymongo import issues**:
   - Lines 14, 22: Cannot find implementation or library stub for module named "pymongo"
   - Import "pymongo" could not be resolved
   - Unused import pymongo

2. **MongoClient possibly-used-before-assignment**:
   - Line 234: Possibly using variable 'MongoClient' before assignment

3. **Broad Exception caught** (multiple lines: 237, 248, 290, 306, 323, 354, 375, 388, 402, 449, 466, 483, 507, 533, 550, 577, 598, 612, 652, 672, 699, 720, 743, 802, 821, 838, 855, 879, 894):
   - Catching too general exception Exception

4. **Logging fstring interpolation** (multiple lines):
   - Use lazy % formatting in logging functions

5. **Line too long** (multiple lines):
   - Line too long (various lengths > 100)

### Fix Plan

1. Use TYPE_CHECKING pattern for optional imports to avoid linter errors
2. Properly initialize MongoClient to None before conditional use
3. Replace broad Exception with specific exception types (sqlite3.Error, ConnectionError, etc.)
4. Replace f-string logging with % formatting
5. Break long lines to comply with 100 character limit

### Status

- [ ] Fix pymongo imports (lines 14, 22)
- [ ] Fix MongoClient initialization (line 234)
- [ ] Fix broad Exception handling (all exception blocks)
- [ ] Fix logging format strings
- [ ] Fix line lengths
