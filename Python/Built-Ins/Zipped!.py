# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/zipped/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================
if __name__ == "__main__":
    st_num, sb_num = map(int, input().strip().split())
    scores = []
    
    for _ in range(sb_num):
        scores.append(map(float, input().strip().split()))
        
    for el in zip(*scores):
        print(sum(el)/sb_num)