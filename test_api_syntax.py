"""Test API Server Syntax"""
import ast
import sys

def check_syntax(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        print(f"{filename}: Syntax OK")
        return True
    except SyntaxError as e:
        print(f"Syntax Error in {filename}: {e}")
        return False

if __name__ == "__main__":
    files = [
        "api_server.py",
        "auth_lib.py", 
        "database_manager.py"
    ]
    all_ok = True
    for f in files:
        if not check_syntax(f):
            all_ok = False
    sys.exit(0 if all_ok else 1)
