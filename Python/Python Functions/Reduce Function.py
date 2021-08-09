from fractions import Fraction
from functools import reduce
# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/reduce-function/problem
# Difficulty: Medium
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================
def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)