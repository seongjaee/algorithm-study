import sys

input = sys.stdin.readline

S = input().rstrip()
postfixes = []
now = ""
for i in range(len(S) - 1, -1, -1):
    now = S[i] + now
    postfixes.append(now)

postfixes.sort()
for postfix in postfixes:
    print(postfix)
