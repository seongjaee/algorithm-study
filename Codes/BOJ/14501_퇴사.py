import sys

input = sys.stdin.readline


def dp(i):
    if i >= n:
        return (0, 0)

    t, p = tp[i]
    if i + t <= n:
        return (max(dp(i + t)) + p, max(dp(i + 1)))
    else:
        return (max(dp(i + 1)), max(dp(i + 1)))


n = int(input())

tp = [tuple(map(int, input().split())) for _ in range(n)]
print(max(dp(0)))
