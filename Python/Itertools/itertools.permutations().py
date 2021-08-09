# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import itertools


s = input().split()
string, number = sorted(s[0]), int(s[1])
print(*list(map(''.join, itertools.permutations(string, number))), sep='\n')