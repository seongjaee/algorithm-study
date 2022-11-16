import sys

input = sys.stdin.readline

h, w, x, y = map(int, input().split())
matrix_B = [list(map(int, input().split())) for _ in range(h + x)]

matrix_A = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        matrix_A[i][j] = matrix_B[i][j]

for i in range(x, h):
    for j in range(y, w):
        matrix_A[i][j] -= matrix_A[i - x][j - y]

for row in matrix_A:
    print(*row)
