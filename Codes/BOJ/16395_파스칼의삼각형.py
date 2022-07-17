import sys

input = sys.stdin.readline

n, k = map(int, input().split())

memo = [[0] * n for _ in range(n)]
memo[0][0] = 1
for i in range(1, n):
    memo[i][0] = 1
    memo[i][i] = 1
    for j in range(1, i):
        memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

print(memo[n - 1][k - 1])
