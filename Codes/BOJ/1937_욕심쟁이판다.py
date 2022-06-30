import sys

input = sys.stdin.readline
sys.setrecursionlimit(50000)

DELTA = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dp(i, j):
    if memo[i][j] != 0:
        return memo[i][j]

    temp = 0
    for di, dj in DELTA:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and matrix[i][j] > matrix[ni][nj]:
            temp = max(dp(ni, nj), temp)

    memo[i][j] = temp + 1
    return temp + 1


n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
memo = [[0] * n for _ in range(n)]

max_value = 1
for i in range(n):
    for j in range(n):
        max_value = max(max_value, dp(i, j))

print(max_value)
