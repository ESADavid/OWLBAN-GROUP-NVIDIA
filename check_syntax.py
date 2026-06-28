import ast
import sys

try:
    with open('auth_lib.py', 'r') as f:
        source = f.read()
    ast.parse(source)
    print('No syntax errors found')
except SyntaxError as e:
    print(f'SyntaxError at line {e.lineno}: {e.msg}')
    print(f'Text: {e.text}')
