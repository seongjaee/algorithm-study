import sys

input = sys.stdin.readline


def delete(col):
    global answer
    for i in range(n):
        if matrix[i][col]:
            print(i, col)
            num, size = matrix[i][col]
            answer += size
            fungus[num] = None
            matrix[i][col] = None
            return


def move():
    next_fungus = {}
    for i in range(k):
        if not fungus[i]:
            continue
        y, x, s, d, b = fungus[i]
        matrix[y][x] = None
        for _ in range(s):
            ny, nx = y + DELTA[d][0], x + DELTA[d][1]
            if ny == -1 or ny == n or nx == -1 or nx == m:
                ny, nx = y - DELTA[d][0], x - DELTA[d][1]
                if d < 2:
                    d = (d + 1) % 2
                else:
                    d = (d + 1) % 2 + 2
            y, x = ny, nx

        if (y, x) in next_fungus and next_fungus[(y, x)][2] > b:
            continue

        next_fungus[(y, x)] = (s, d, b, i)

    new_fungus = [None] * k
    for (y, x), (s, d, b, i) in next_fungus.items():
        matrix[y][x] = (i, b)
        new_fungus[i] = (y, x, s, d, b)

    return new_fungus


DELTA = [(-1, 0), (1, 0), (0, 1), (0, -1)]

n, m, k = map(int, input().split())
matrix = [[None] * m for _ in range(n)]
fungus = [None] * k
for i in range(k):
    y, x, s, d, b = map(int, input().split())
    matrix[y - 1][x - 1] = (i, b)
    fungus[i] = (y - 1, x - 1, s, d - 1, b)

answer = 0
for j in range(m):
    delete(j)
    fungus = move()

print(answer)
