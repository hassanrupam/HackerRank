# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/whats-your-name/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def print_full_name(first_name, last_name):
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))
    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)