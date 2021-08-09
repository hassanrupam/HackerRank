# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import numpy 

n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print(array.transpose())
print(array.flatten())