# Auth Library Fixes TODO

## Plan to fix linting errors in auth_lib.py

### Step 1: Fix Mypy type errors (Implicit Optional)

- [x] Read the file
- [ ] Line 225: Change `ip_address: str = None` to `ip_address: Optional[str] = None`
- [ ] Line 226: Change `user_agent: str = None` to `user_agent: Optional[str] = None`
- [ ] Line 312: Same fixes in create_session
- [ ] Line 382: Change `company: str = None` to `company: Optional[str] = None`
- [ ] Line 451: Same fixes for ip_address, user_agent
- [ ] Line 458: Change `permissions: list[str] = None` to `permissions: Optional[List[str]] = None`

### Step 2: Fix Pylint - file encoding

- [ ] Line 130: Add encoding='utf-8' to open()
- [ ] Line 142: Add encoding='utf-8' to open()

### Step 3: Fix Pylint - broad exception catching

- [ ] Line 132: Catch more specific exceptions
- [ ] Line 144: Catch more specific exceptions

### Step 4: Fix Pylint - logging f-string interpolation

- [ ] Lines 133, 145, 222, 230, 242, 244, 253, 332, 353, 370, 378, 407, 417, 428, 443: Change f-strings to lazy % formatting

### Step 5: Fix Pylint - redefined outer names

- [ ] Lines 203, 210, 228, 256, 280, 281, 288, 295, 298, 302, 312, 361, 385, 411, 421, 433: Rename local variables

### Step 6: Fix Pylint - missing docstrings

- [ ] Lines 43, 52, 451, 454, 457, 461: Add docstrings

### Step 7: Fix Pylint - line too long

- [ ] Lines 96, 165, 176, 241, 269, 277, 281, 298, 477: Break long lines

### Step 8: Fix Pylint - trailing whitespace

- [ ] Lines 440, 444: Remove trailing whitespace
