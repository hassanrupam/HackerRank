# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================


import numpy

numpy.set_printoptions(sign=' ')

a = numpy.array(input().split(), float)
print(*(f(a) for f in [numpy.floor, numpy.ceil, numpy.rint]), sep='\n')