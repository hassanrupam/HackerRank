# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/exceptions/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================


for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except BaseException as err:
        print("Error Code:", err)