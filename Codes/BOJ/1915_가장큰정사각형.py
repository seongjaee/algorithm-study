# top-down
import sys

input = sys.stdin.readline


def dp(i, j):
    if memo[i][j]:
        return memo[i][j]

    if i == 0 or j == 0:
        memo[i][j] = matrix[i][j]
        return memo[i][j]

    if matrix[i][j] == 0:
        return 0

    else:
        memo[i][j] = min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1
        return memo[i][j]


n, m = map(int, input().split())

matrix = [list(map(int, input().rstrip())) for _ in range(n)]
memo = [[0] * m for _ in range(n)]

max_value = 0
for i in range(n):
    for j in range(m):
        max_value = max(max_value, dp(i, j))

print(max_value**2)


# bottom-up
import sys

input = sys.stdin.readline


n, m = map(int, input().split())

matrix = [list(map(int, input().rstrip())) for _ in range(n)]
memo = [[0] * m for _ in range(n)]
max_value = 0

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            memo[i][j] = matrix[i][j]
        elif matrix[i][j]:
            memo[i][j] = min(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1]) + 1
        max_value = max(max_value, memo[i][j])

print(max_value**2)
