# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-split/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

regex_pattern = r"[.,]+"    # Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))