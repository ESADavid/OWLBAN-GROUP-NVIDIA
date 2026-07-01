#!/usr/bin/env python3
"""Fix pylint errors in database_manager.py"""

import re


def fix_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace f-string logging with % formatting
    content = re.sub(
        r'self\.logger\.error\(f"([^"]+): \{e\}"\)',
        r'self.logger.error("%s: %s", r"\1", e)',
        content
    )
    content = re.sub(
        r'self\.logger\.warning\(f"([^"]+): \{e\}"\)',
        r'self.logger.warning("%s: %s", r"\1", e)',
        content
    )

    # Fix .keys() iteration
    content = re.sub(
        r'for key in (\w+)\.keys\(\):',
        r'for key in \1:',
        content
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed file written to {output_path}")


if __name__ == "__main__":
    fix_file("database_manager.py", "database_manager_fixed.py")
