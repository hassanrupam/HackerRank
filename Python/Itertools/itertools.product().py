# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/itertools-product/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

from itertools import product


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*list(product(a, b)))