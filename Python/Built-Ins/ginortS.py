# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/ginorts/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ========================

if __name__ == "__main__":
    string = input().strip()
    
    print(*sorted(string, key = lambda x: (-x.islower(), x.isdigit() - x.isupper(), x in '02468', x)), sep='')