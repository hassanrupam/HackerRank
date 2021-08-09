# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/incorrect-regex/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re


for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print('False')