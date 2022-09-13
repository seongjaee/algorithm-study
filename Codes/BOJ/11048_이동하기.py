import sys

input = sys.stdin.readline


n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = matrix[0][0]
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + matrix[i][0]
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + matrix[0][j]


for i in range(1, n):
    for j in range(1, m):
        temp = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        dp[i][j] = matrix[i][j] + temp

print(dp[-1][-1])
