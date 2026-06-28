#!/usr/bin/env python3
"""Fix indentation issues in auth_lib.py"""

# Read the file
with open('auth_lib.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: session_data line in _load_data - need to add proper indentation
old_str1 = (
    "with open(self.session_store_file, 'r', encoding='utf-8') as f:\n"
    "session_data = json.load(f)"
)
new_str1 = (
    "with open(self.session_store_file, 'r', encoding='utf-8') as f:\n"
    "                    session_data = json.load(f)"
)
content = content.replace(old_str1, new_str1)

# Fix 2: session = Session in create_session
old_str2 = "now = datetime.now(timezone.utc)\nsession = Session("
new_str2 = "now = datetime.now(timezone.utc)\n        session = Session("
content = content.replace(old_str2, new_str2)

# Write back
with open('auth_lib.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed indentation issues")
