# Read lines 183-200 from auth_lib.py
with open('auth_lib.py', 'r') as f:
    lines = f.readlines()
    for i in range(182, 200):
        if i < len(lines):
            print(str(i+1) + ": " + lines[i], end='')
