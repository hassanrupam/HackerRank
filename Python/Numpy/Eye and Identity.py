# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/np-eye-and-identity/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================
import numpy

numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))