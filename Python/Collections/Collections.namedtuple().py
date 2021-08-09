# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

from collections import namedtuple


n, Student = int(input()), namedtuple('Student', input())
print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n))