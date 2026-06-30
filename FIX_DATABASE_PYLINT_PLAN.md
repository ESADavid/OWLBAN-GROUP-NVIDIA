# Database Manager Pylint Fix Plan

## Issues to Fix

### 1. W0718:broad-exception-caught

Replace generic `except Exception:` with more specific exception types:

- sqlite3.Error for SQLite operations
- json.JSONDecodeError for JSON operations  
- redis.RedisError for Redis operations
- ConnectionError for network operations
- ValueError for validation errors

### 2. W1203:logging-fstring-interpolation

Replace f-strings in logging with lazy % formatting:

- `self.logger.error(f"message: {e}")` → `self.logger.error("message: %s", e)`

### 3. C0301:line-too-long

Break lines longer than 100 characters using:

- Line continuation with parentheses
- Split into multiple assignments
- Use intermediate variables

### 4. C0201:consider-iterating-dictionary

Replace `for key in dictionary.keys():` with `for key in dictionary:`

## Line Numbers to Fix

- Line 80-81: broad-exception + logging fstring
- Line 231-232: broad-exception + logging fstring
- Line 242-243: broad-exception + logging fstring
- Line 284-285: broad-exception + logging fstring
- Line 300-301: broad-exception + logging fstring
- Line 317-318: broad-exception + logging fstring
- Line 348-349: broad-exception + logging fstring
- Line 369-370: broad-exception + logging fstring
- Line 382-383: broad-exception + logging fstring
- Line 396-397: broad-exception + logging fstring
- Line 443-444: broad-exception + logging fstring
- Line 460-461: broad-exception + logging fstring
- Line 477-478: broad-exception + logging fstring
- Line 501: broad-exception
- Line 527-528: broad-exception + logging fstring
- Line 544-545: broad-exception + logging fstring
- Line 571-572: broad-exception + logging fstring
- Line 592-593: broad-exception + logging fstring
- Line 606-607: broad-exception + logging fstring
- Line 662-663: broad-exception + logging fstring
- Line 682-683: broad-exception + logging fstring
- Line 709-710: broad-exception + logging fstring
- Line 730731: broad-exception + logging fstring
- Line 753-754: broad-exception + logging fstring
- Lines 582, 720: .keys() iteration
- Line 238: Line too long (152/100)
- Line 304: Line too long (108/100)
- Line 312: Line too long (111/100)
- Line 321: Line too long (103/100)
- Line 330: Line too long (101/100)
- Line 334: Line too long (101/100)
- Line 353: Line too long (109/100)
- Line 401: Line too long (101/100)
- Line 406: Line too long (111/100)
- Line 410: Line too long (117/100)
- Line 464: Line too long (115/100)
- Line 472: Line too long (125/100)
- Line 492: Line too long (108/100)
- Line 500: Line too long (102/100)
- Line 521: Line too long (132/100)
- Line 523: Line too long (107/100)
- Line 548: Line too long (128/100)
- Line 587: Line too long (107/100)
- Line 647: Line too long (107/100)
- Line 654: Line too long (103/100)
- Line 657: Line too long (105/100)
- Line 725: Line too long (115/100)
- Line 747: Line too long (111/100)
- Line 749: Line too long (108/100)
- Line 761: Line too long (108/100)
- Line 762: Line too long (103/100)
- Line 763: Line too long (109/100)
- Line 792-796: Line too long (multiple)
- Line 799: Line too long (101/100)

## Implementation Strategy

1. Create fixed version of database_manager.py
2. Fix all broad-exception errors
3. Fix all logging fstring errors  
4. Fix line-too-long issues
5. Fix dictionary iteration issues
6. Test the fixed version
