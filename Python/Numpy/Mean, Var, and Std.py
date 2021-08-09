# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================


import numpy

N, M = map(int, input().strip().split())

my_array = numpy.array([ input().strip().split() for _ in range(N) ], int)

print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None),11))