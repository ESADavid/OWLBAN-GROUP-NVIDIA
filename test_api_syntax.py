import ast
import sys

# Check api_server.py syntax
try:
    with open('api_server.py', 'r') as f:
        source = f.read()
    ast.parse(source)
    print('api_server.py: No syntax errors found')
except SyntaxError as e:
    print(f'api_server.py: SyntaxError at line {e.lineno}: {e.msg}')
    sys.exit(1)

print('All syntax checks passed!')
