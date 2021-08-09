# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-start-re-end/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================
import re

if __name__ == "__main__":
    string = input()
    sub = input()
    
    matches = list(re.finditer(r'(?={})'.format(sub), string))
    
    if matches:
        for match in matches:
            print((match.start(), match.end() + len(sub) - 1))
    else:
        print((-1, -1))