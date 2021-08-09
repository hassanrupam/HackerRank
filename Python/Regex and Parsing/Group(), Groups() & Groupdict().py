# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-group-groups/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

if __name__ == "__main__":
    string = input()
    
    match = re.search(r'([a-zA-Z0-9])\1+', string)
    
    print(match.group(1) if match else -1)