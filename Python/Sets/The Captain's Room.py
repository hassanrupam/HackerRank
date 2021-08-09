# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================
k = int(input())
room_number_list = list(map(int, input().split()))
captain_room_number = (sum(set(room_number_list)) * k - sum(room_number_list)) // (k - 1)
print(captain_room_number)