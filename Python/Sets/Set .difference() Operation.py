# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.difference(b)))