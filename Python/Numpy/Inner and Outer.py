# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/np-inner-and-outer/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A, B), numpy.outer(A, B), sep='\n')