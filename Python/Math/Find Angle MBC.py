# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/find-angle/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

from math import atan
from math import degrees

if __name__ == "__main__":
    ab = int(input().strip())
    bc = int(input().strip())
    
    print("{}\N{DEGREE SIGN}".format(int(round(degrees(atan(ab/bc))))))