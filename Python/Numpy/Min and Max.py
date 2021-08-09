# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/np-min-and-max/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================
import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.max(numpy.min(A, axis=1), axis=0))