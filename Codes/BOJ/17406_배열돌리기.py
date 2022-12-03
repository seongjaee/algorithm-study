import sys
from itertools import permutations as pmts
from copy import deepcopy


def spin(sy, sx, s, matrix):
    def spin_one_line(sy, sx, ey, ex, matrix):
        if sy == ey:
            return

        temp = matrix[sy][sx]
        for y in range(sy, ey):
            matrix[y][sx] = matrix[y + 1][sx]

        for x in range(sx, ex):
            matrix[ey][x] = matrix[ey][x + 1]

        for y in range(ey, sy, -1):
            matrix[y][ex] = matrix[y - 1][ex]

        for x in range(ex, sx, -1):
            matrix[sy][x] = matrix[sy][x - 1]

        matrix[sy][sx + 1] = temp

    for i in range(s + 1):
        spin_one_line(sy + i, sx + i, sy + s * 2 - i, sx + s * 2 - i, matrix)


input = sys.stdin.readline
n, m, k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
cmds = []
for _ in range(k):
    r, c, s = map(int, input().split())
    sr, sc = r - s - 1, c - s - 1
    cmds.append((sr, sc, s))

answer = 1e10

permutations = list(pmts(cmds))
for p in permutations:
    new_matrix = deepcopy(matrix)

    for sr, sc, s in p:
        spin(sr, sc, s, new_matrix)

    value = min([sum(row) for row in new_matrix])
    answer = min(answer, value)

print(answer)
