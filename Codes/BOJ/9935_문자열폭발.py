import sys

input = sys.stdin.readline

s = input().rstrip()
bomb = list(input().rstrip())
l = len(bomb)

stack = []
for char in s:
    stack.append(char)
    if stack[-l:] == bomb:
        for _ in range(l):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
