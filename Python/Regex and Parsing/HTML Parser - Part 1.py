# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/html-parser-part-1/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start".ljust(6) + ":", tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))
    def handle_endtag(self, tag):
        print("End".ljust(6) + ":", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty".ljust(6) + ":", tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))

if __name__ == "__main__":
    parser = MyHTMLParser()
    n = int(input().strip())
    for _ in range(n):
        line = input()
        parser.feed(line)