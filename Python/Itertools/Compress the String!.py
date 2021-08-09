# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/compress-the-string/problem
# Difficulty: Medium
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

from itertools import groupby


print(*[(len(list(c)), int(x)) for x, c in groupby(input())])