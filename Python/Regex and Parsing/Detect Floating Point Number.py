# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/introduction-to-regex/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================


import re

if __name__ == "__main__":
    t = int(input().strip())
    pattern = '^[+-]?[0-9]*\.[0-9]+$'
    
    for _ in range(t):
        print(bool(re.match(pattern, input())))