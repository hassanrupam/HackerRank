# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
# Difficulty: Medium
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

def change(match):
    symb = match.group(0)
    
    if symb == "&&":
        return "and"
    elif symb == "||":
        return "or"
    
n = int(input().strip())
for _ in range(n):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', change, input()))