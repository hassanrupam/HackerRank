# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]


html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()