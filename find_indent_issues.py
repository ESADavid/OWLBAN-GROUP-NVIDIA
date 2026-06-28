#!/usr/bin/env python3
"""Find all indentation issues in a Python file."""

import ast
import tokenize


def check_indentation(filename):
    """Check for indentation issues in a Python file."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try to detect the base indentation used
    lines = content.split('\n')
    indent_sizes = {}

    for _, line in enumerate(lines, 1):
        if line.strip() and not line.strip().startswith('#'):
            stripped = line.lstrip()
            indent = len(line) - len(stripped)
            if indent > 0 and indent % 4 == 0:
                indent_sizes[indent] = indent_sizes.get(indent, 0) + 1

    # Show indentation distribution
    print(f"Indentation distribution in {filename}:")
    for indent in sorted(indent_sizes.keys()):
        print(f"  {indent} spaces: {indent_sizes[indent]} lines")

    # Now do a token-level parse to find exact issues
    print("\nParsing tokens...")

    try:
        tokens = list(tokenize.generate_tokens(iter(content.splitlines(keepends=True)).__next__))
        print(f"  Found {len(tokens)} tokens")
    except tokenize.TokenError as e:
        print(f"Token error: {e}")
    except IndentationError as e:
        print(f"IndentationError at line {e.lineno}: {e.msg}")
        print(f"  Text: {e.text}")

    # More detailed check using AST
    print("\nAttempting AST parse...")
    try:
        ast.parse(content)
        print("  AST: No syntax errors!")
    except SyntaxError as e:
        print(f"  AST Error at line {e.lineno}: {e.msg}")
        if hasattr(e, 'text') and e.text:
            print(f"    Text: {e.text}")


if __name__ == '__main__':
    check_indentation('auth_lib.py')
