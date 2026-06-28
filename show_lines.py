"""Display specific lines from auth_lib.py for analysis"""
with open('auth_lib.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
# Display lines around the Optional type issues
for i in range(310, 320):
    print(f"{i+1}: {lines[i]}", end='')
print("\n--- Line 380-390 ---")
for i in range(379, 390):
    print(f"{i+1}: {lines[i]}", end='')
print("\n--- Line 448-465 ---")
for i in range(447, 465):
    print(f"{i+1}: {lines[i]}", end='')
