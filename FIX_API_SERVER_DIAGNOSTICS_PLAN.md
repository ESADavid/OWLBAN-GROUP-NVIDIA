# FIX API_SERVER.PY DIAGNOSTICS PLAN

## Issues Summary

### Critical (Errors - Must Fix)
1. **Function Redefinition** (no-redef) - Lines 49, 57, 66, 77
   - `authenticate_user` is imported and also defined as fallback
   - `create_user` is imported and also defined as fallback  
   - `verify_token` is imported and also defined as fallback

2. **Type Assignment** (assignment) - Line 55
   - `auth_manager = None` but variable expects `AuthManager`

3. **Argument Type Mismatch** (arg-type) - Line 348
   - `permissions: list[str] | None` expected `list[str]`

4. **Default Argument Type** - Line 911
   - `data` default `None` expected `dict[str, Any]`

### Warnings (Should Fix)
1. **global-statement** - Line 175
2. **broad-exception-caught** - Multiple lines (183, 192, 199, 206, 361, 404, 440, 504, etc.)
3. **unused-import** - Line 884

### Conventions (Nice to Have)
1. Missing docstrings on many classes and functions
2. Line too long issues (multiple lines)
3. Trailing whitespace
4. Import grouping

## Fix Plan

### Step 1: Fix Function Redefinition
Move fallback functions inside the `except ImportError` block so they're only defined when auth_lib is not available.

**Before:**
```python
try:
    from auth_lib import authenticate_user, create_user, verify_token
    from auth_lib import auth_manager as _auth_manager
    AUTH_AVAILABLE = True
except ImportError:
    AUTH_AVAILABLE = False
    _auth_manager = None

# Fallback functions (UNCONDITIONAL - CAUSES REDEFINITION)
def authenticate_user(...):
    ...
def create_user(...):
    ...
def verify_token(...):
    ...
```

**After:**
```python
try:
    from auth_lib import authenticate_user, create_user, verify_token
    from auth_lib import auth_manager as _auth_manager
    AUTH_AVAILABLE = True
except ImportError:
    AUTH_AVAILABLE = False
    _auth_manager = None
    
    # Fallback functions (CONDITIONAL - FIXES REDEFINITION)
    def authenticate_user(...):
        ...
    def create_user(...):
        ...
    def verify_token(...):
        ...
```

### Step 2: Fix Type Assignment
Add Optional type hint or use typing.TypeVar.

**Current:**
```python
_auth_manager = None  # Line 55
```

**Fix:**
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from auth_lib import AuthManager

_auth_manager: Optional["AuthManager"] = None
```

Or simply use `Any` type:
```python
_auth_manager: Any = None
```

### Step 3: Fix create_user call at line 348
The call uses `permissions=user_data.permissions` which can be None.

**Fix options:**
1. Change function signature to accept Optional[List[str]]
2. Add default: `permissions: list[str] = []`

### Step 4: Fix default argument at line 911
Change `data: dict[str, Any] = None` to use empty dict or Optional.

## Files to Modify
- `api_server.py`

## Testing After Fix
Run pylint and mypy to verify:
```bash
pylint api_server.py
mypy api_server.py
