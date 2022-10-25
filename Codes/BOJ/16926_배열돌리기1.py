import sys

input = sys.stdin.readline


def spin_one_line(x):
    temp = matrix[x][x]
    for j in range(x, m - x - 1):
        matrix[x][j] = matrix[x][j + 1]

    for i in range(x, n - x - 1):
        matrix[i][m - x - 1] = matrix[i + 1][m - x - 1]

    for j in range(m - x - 1, x, -1):
        matrix[n - x - 1][j] = matrix[n - x - 1][j - 1]

    for i in range(n - x - 1, x, -1):
        matrix[i][x] = matrix[i - 1][x]

    matrix[x + 1][x] = temp


def spin():
    for i in range(k):
        spin_one_line(i)


n, m, r = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
k = min(n, m) // 2

for _ in range(r):
    spin()

for row in matrix:
    print(*row)
