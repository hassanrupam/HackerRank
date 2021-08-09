#!/bin/python3

import math
import os
import random
import re
import sys
# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/capitalize/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
