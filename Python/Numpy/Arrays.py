import numpy
# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/np-arrays/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================
def arrays(arr):
    return (numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)