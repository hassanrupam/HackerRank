# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))