# Fix Pylint Diagnostics TODO

## Overview

Fix linting errors in auth_lib.py and api_server.py based on diagnostic output

## Priority 1: Critical Type Errors (Mypy)

- [x] 1. auth_lib.py line 208: permissions = None should use Optional[List[str]]
- [x] 2. auth_lib.py line 573: Same issue
- [ ] 3. auth_lib.py line 519: CSRFToken keyword arguments

## Priority 2: Pylint Warnings - Broad Exception Catching

- [x] 1. auth_lib.py line 133: except Exception
- [x] 2. auth_lib.py line 141: except Exception
- [x] 3. auth_lib.py line 150: except Exception
- [x] 4. auth_lib.py line 162: except Exception
- [x] 5. api_server.py line 255: except Exception
- [x] 6. api_server.py line 264: except Exception
- [x] 7. api_server.py line 271: except Exception
- [x] 8. api_server.py line 278: except Exception
- [x] 9. api_server.py line 433: except Exception
- [x] 10. api_server.py line 476: except Exception

## Priority 3: Variable Shadowing

- [x] 1. auth_lib.py line 220: message redefined
- [x] 2. auth_lib.py line 227: user redefined
- [x] 3. auth_lib.py line 297: access_token redefined
- [x] 4. auth_lib.py line 298: refresh_token redefined
- [x] 5. api_server.py line 158: HTTPException redefined

## Priority 4: Unused Arguments

- [x] 1. auth_lib.py line 242: ip_address unused
- [x] 2. auth_lib.py line 243: user_agent unused

## Priority 5: Style Issues

- [ ] 1. Missing function docstrings (multiple)
- [ ] 2. Line too long (check after fixes)
- [x] 3. Trailing whitespace (multiple lines)
- [x] 4. Consider f-strings

## Status: Started

- Created FIX_PYLINT_DIAGNOSTICS_TODO.md
- Fixed basic issues via edit_file
- Continue with remaining issues
