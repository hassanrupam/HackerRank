# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/np-polynomials/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import numpy

poly = [float(x) for x in input().split()]
x = float(input())
print(numpy.polyval(poly, x))