import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]

presum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(1, m + 1):
        presum[i + 1][j] += presum[i][j] + matrix[i][j - 1]

for i in range(1, n + 1):
    for j in range(m):
        presum[i][j + 1] += presum[i][j]

k = int(input())
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    print(
        presum[y2][x2]
        - presum[y2][x1 - 1]
        - presum[y1 - 1][x2]
        + presum[y1 - 1][x1 - 1]
    )
