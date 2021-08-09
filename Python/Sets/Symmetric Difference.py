# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================


i, m = input(), set(map(int, input().split()))
i, n = input(), set(map(int, input().split()))
print(*sorted(m.symmetric_difference(n)), sep='\n')