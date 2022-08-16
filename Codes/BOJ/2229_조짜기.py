import sys

input = sys.stdin.readline

n = int(input())
numbers = [*map(int, input().split())]


def dp(j):
    if memo[j] != -1:
        return memo[j]

    temp = max_i2j[0][j] - min_i2j[0][j]
    for i in range(j):
        temp = max(temp, dp(i) + max_i2j[i + 1][j] - min_i2j[i + 1][j])

    memo[j] = temp
    return temp


max_i2j = [[0] * n for _ in range(n)]
min_i2j = [[10001] * n for _ in range(n)]
for i in range(n):
    max_i2j[i][i] = numbers[i]
    min_i2j[i][i] = numbers[i]
    for j in range(i + 1, n):
        max_i2j[i][j] = max(max_i2j[i][j - 1], numbers[j])
        min_i2j[i][j] = min(min_i2j[i][j - 1], numbers[j])


memo = [-1] * n
memo[0] = 0

print(dp(n - 1))
