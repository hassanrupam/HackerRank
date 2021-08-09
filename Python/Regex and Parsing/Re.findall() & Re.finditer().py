# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

cons = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
vowels = 'AEIOUaeiou'

if __name__ == "__main__":
    string = input().strip()
    
    m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (cons, vowels, cons), string)
    
    print("\n".join(m or ['-1']))