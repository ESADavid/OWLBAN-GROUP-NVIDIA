# TODO: Fix Pylint/Pylance Issues in database_manager.py

## Status: In Progress

### Issues to Fix

1. **[FIXED]** Unused import pymongo - Remove unused pymongo import
2. **[IN PROGRESS]** Broad exception caught (W0718) - Replace broad `except Exception` with more specific exceptions
3. **[PENDING]** Logging fstring interpolation (W1203) - Convert f-strings to lazy % formatting
4. **[PENDING]** Line too long (C0301) - Break lines exceeding 100 characters
5. **[PENDING]** Consider iterating dictionary (C0201) - Iterate dict directly instead of .keys()

### Progress

- [x] Remove unused pymongo import
- [ ] Fix all broad Exception catches
- [ ] Fix all logging fstring interpolations
- [ ] Break all long lines
- [ ] Fix dictionary iterations

### Notes

- Total exceptions to fix: ~30 occurrences
- Total logging issues: ~30 occurrences  
- Total long lines: ~30 occurrences
- Total dict iteration issues: 2 occurrences
