import sys

input = sys.stdin.readline


n = int(input())

tp = [tuple(map(int, input().split())) for _ in range(n)]

memo = [(0, 0)] * (n + 1)
for i in range(n - 1, -1, -1):
    t, p = tp[i]
    if i + t <= n:
        memo[i] = (max(memo[i + t]) + p, max(memo[i + 1]))
    else:
        memo[i] = (max(memo[i + 1]), max(memo[i + 1]))

print(max(memo[0]))
