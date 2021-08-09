# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# Difficulty: Medium
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ======================== 
import re

def fun(email):
    pattern = '^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)