# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/the-minion-game/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ======================== 
vowels = ['A', 'E', 'I', 'O', 'U']

def minion_game(string):
    score_kevin = 0
    score_stuart = 0
    
    for ind in range(len(string)):
        if string[ind] in vowels:
            score_kevin += len(string) - ind
        else:
            score_stuart += len(string) - ind
    
    if score_kevin > score_stuart:
        print("Kevin {}".format(score_kevin))
    elif score_kevin < score_stuart:
        print("Stuart {}".format(score_stuart))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)