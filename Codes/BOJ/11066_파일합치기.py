import sys

input = sys.stdin.readline


def dp(i, j):
    if memo[i][j] != -1:
        return memo[i][j]
    if i == j:
        memo[i][j] = 0
        return 0

    memo[i][j] = (
        min([dp(i, x) + dp(x + 1, j) for x in range(i, j)]) + presum[j + 1] - presum[i]
    )
    return memo[i][j]


t = int(input())
for _ in range(t):
    k = int(input())
    numbers = [*map(int, input().split())]
    presum = [0]
    for i in range(k):
        presum.append(presum[i] + numbers[i])

    memo = [[-1] * k for _ in range(k)]
    print(dp(0, k - 1))
