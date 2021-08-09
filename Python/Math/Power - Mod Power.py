# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-power-mod-power/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

a=int(input())
b=int(input())
m=int(input())
pro = 1;
for i in range(b):
    pro*=a
print(pro)
print(pro%m)