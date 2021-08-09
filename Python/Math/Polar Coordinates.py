#!/usr/bin/env python3
# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/polar-coordinates/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================
import cmath

if __name__ == "__main__":
    cnum = complex(input().strip())
    
    print(abs(cnum))
    print(cmath.phase(cnum))