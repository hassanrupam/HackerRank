# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

a=int(input())
if(a>=1 and a<=1000):
    b=int(input())
    if(b>=1 and b<=1000):
        c= int(input())
        if(c>=1 and c<=1000):
            d=int(input())
res = pow(a,b)+pow(c,d)
print(res)