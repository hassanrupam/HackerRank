# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/validating-credit-card-number/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ========================
import re

pattern = re.compile(
    r'^'
    r'(?!.*(\d)(-?\1){3})'
    r'[456]\d{3}'
    r'(?:-?\d{4}){3}'
    r'$')
for _ in range(int(input().strip())):
    print('Valid' if pattern.search(input().strip()) else 'Invalid')