import sys

input = sys.stdin.readline


def dp(i, j):
    if memo[i][j]:
        return memo[i][j]

    cnt = 0
    for y in range(i - 1, -1, -1):
        if matrix[y][j] + y == i:
            cnt += dp(y, j)

    for x in range(j - 1, -1, -1):
        if matrix[i][x] + x == j:
            cnt += dp(i, x)

    memo[i][j] = cnt
    return cnt


n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]

memo = [[0] * n for _ in range(n)]
memo[0][0] = 1

print(dp(n - 1, n - 1))
