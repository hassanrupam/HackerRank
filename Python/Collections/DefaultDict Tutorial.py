
# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

from collections import defaultdict


n, m = map(int, input().split())
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(str(i))
for i in range(m):
    print(' '.join(d[input()]) or -1)