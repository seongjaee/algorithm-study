import sys

input = sys.stdin.readline

n = int(input())

before = {input().rstrip(): i for i in range(n)}
after = [input().rstrip() for _ in range(n)]

answer = 0
min_value = n
for i in range(n - 1, -1, -1):
    if min_value < before[after[i]]:
        answer += 1
    else:
        min_value = before[after[i]]

print(answer)
