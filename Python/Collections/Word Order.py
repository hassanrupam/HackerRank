# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/word-order/problem
# Difficulty: Medium
# Max Score: 50
# Language: Python

# ========================
#         Solution
# ========================

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


ordered_counter = OrderedCounter(input() for _ in range(int(input())))
print(len(ordered_counter))
print(*ordered_counter.values())