# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-check-subset/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

for i in range(int(input())):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(a.issubset(b))