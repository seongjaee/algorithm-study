import sys

input = sys.stdin.readline


def partial_sum(i, j, x, y):
    result = 0
    for r in range(i - 1, x):
        for c in range(j - 1, y):
            result += matrix[r][c]
    return result


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

presum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        presum[i][j] += presum[i - 1][j] + matrix[i - 1][j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        presum[i][j] += presum[i][j - 1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(presum[x][y] + presum[i - 1][j - 1] - presum[x][j - 1] - presum[i - 1][y])
