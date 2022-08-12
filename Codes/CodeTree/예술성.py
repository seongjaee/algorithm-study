from copy import deepcopy
import sys

input = sys.stdin.readline


def get_score(matrix):
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return
        elif x < y:
            parents[y] = x
            sizes[x[0]][x[1]] += sizes[y[0]][y[1]]
        else:
            parents[x] = y
            sizes[y[0]][y[1]] += sizes[x[0]][x[1]]

    parents = {(i, j): (i, j) for i in range(n) for j in range(n)}
    sizes = [[1] * n for _ in range(n)]

    between_cnt = {}
    for i in range(n):
        for j in range(n):
            for di, dj in DELTA:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue
                if find((i, j)) == find((ni, nj)):
                    continue
                if matrix[i][j] == matrix[ni][nj]:
                    union((i, j), (ni, nj))

    total_score = 0
    for i in range(n):
        for j in range(n):
            if i + 1 < n and matrix[i][j] != matrix[i + 1][j]:
                p1 = find((i, j))
                p2 = find((i + 1, j))
                p1, p2 = min(p1, p2), max(p1, p2)
                between_cnt[(p1, p2)] = between_cnt.get((p1, p2), 0) + 1

            if j + 1 < n and matrix[i][j] != matrix[i][j + 1]:
                p1 = find((i, j))
                p2 = find((i, j + 1))
                p1, p2 = min(p1, p2), max(p1, p2)
                between_cnt[(p1, p2)] = between_cnt.get((p1, p2), 0) + 1

    for key, value in between_cnt.items():
        a, b = key
        ay, ax = a
        by, bx = b

        score = (
            (sizes[ay][ax] + sizes[by][bx]) * matrix[ay][ax] * matrix[by][bx] * value
        )
        total_score += score

    return total_score


def spin():
    mid = n // 2
    # 십자
    for i in range(mid):
        (
            matrix[mid][i],
            matrix[n - 1 - i][mid],
            matrix[mid][n - 1 - i],
            matrix[i][mid],
        ) = (
            matrix[i][mid],
            matrix[mid][i],
            matrix[n - 1 - i][mid],
            matrix[mid][n - 1 - i],
        )

    rotate()


def rotate():
    global matrix
    new_matrix = deepcopy(matrix)

    mid = n // 2
    for sy, sx, ey, ex in [
        (0, 0, mid - 1, mid - 1),
        (0, mid + 1, mid - 1, n - 1),
        (mid + 1, 0, n - 1, mid - 1),
        (mid + 1, mid + 1, n - 1, n - 1),
    ]:
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                new_matrix[y][x] = matrix[ey - x + sx][sx + y - sy]

    matrix = new_matrix


DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]

answer = 0
for i in range(4):
    answer += get_score(matrix)
    if i == 3:
        break
    spin()

print(answer)
