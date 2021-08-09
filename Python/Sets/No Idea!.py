# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/no-idea/problem
# Difficulty: Medium
# Max Score: 50
# Language: Python

# ========================
#         Solution
# ========================



_ = input()
array = input().split()
like = set(input().split())
dislike = set(input().split())
print(sum((i in like) - (i in dislike) for i in array))