# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/np-concatenate/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================
import numpy

a, b, c = map(int, input().split())
A = numpy.array([input().split() for _ in range(a)], int)
B = numpy.array([input().split() for _ in range(b)], int)
print(numpy.concatenate((A, B), axis=0))