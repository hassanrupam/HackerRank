# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/input/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================
if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    string = input().strip()
    
    if eval(string) == k:
        print(True)
    else:
        print(False)