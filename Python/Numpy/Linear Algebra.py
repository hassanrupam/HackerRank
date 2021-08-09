# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/np-linear-algebra/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================
import numpy
numpy.set_printoptions(legacy='1.13')

n = int(input())
array = numpy.array([input().split() for _ in range(n)], float)
print(numpy.linalg.det(array))