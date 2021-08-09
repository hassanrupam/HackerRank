# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================


import re

t = int(input().strip())
for _ in range(t):
    name, email = input().strip().split()
    
    if re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email):
        print("{} {}".format(name, email))