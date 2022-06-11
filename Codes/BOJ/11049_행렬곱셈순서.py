import sys

input = sys.stdin.readline

INF = 2**31

# i번째 행렬부터 j번째 행렬까지 곱 최소 연산 수
def dp(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return INF
    if memo[i][j] != INF:
        return memo[i][j]
    if i == j:
        memo[i][j] = 0
        return 0

    min_value = INF
    for k in range(i, j):
        min_value = min(
            min_value, dp(i, k) + dp(k + 1, j) + sizes[i][0] * sizes[k][1] * sizes[j][1]
        )

    memo[i][j] = min_value
    return min_value


n = int(input())
sizes = [tuple(map(int, input().split())) for _ in range(n)]
memo = [[INF] * n for _ in range(n)]

print(dp(0, n - 1))
# print(memo)
